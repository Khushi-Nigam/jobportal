from django.shortcuts import render,redirect,get_object_or_404
from . models import Login,Employer,JobSeeker,Enquiry,Job,Application
from adminapp.models import News
from employer.models import Jobs
from django.core.exceptions import ObjectDoesNotExist
import datetime
from jobapp.utils import send_notification
from django.contrib.auth.models import User
from jsapp.models import JobSeekerDetails
from jobapp.models import Job,Application
from jobapp.utils import send_notification
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def index(request):
    job=Jobs.objects.all()
    return render(request,"index.html",locals())
def aboutus(request):
    return render(request,"aboutus.html")
def jobseekerreg(request):
    if request.method=="POST":
        profilepic=request.POST["profilepic"]
        name=request.POST["name"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        contactno=request.POST["contactno"]
        emailaddress=request.POST["emailaddress"]
        password=request.POST["password"]
        dob=request.POST["dob"]
        regdate=datetime.datetime.today()
        jobseek=JobSeeker(profilepic=profilepic,name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,dob=dob,regdate=regdate)
        jobseek.save()
        log=Login(username=emailaddress,password=password,usertype="jobseeker")
        log.save()
        return render(request,"jobseeker.html",{"msg":"Registration is done"})
    return render(request,"jobseeker.html")
def login(request):
    if request.method=="POST":  
        username=request.POST["username"]
        password=request.POST["password"]
        usertype=request.POST['usertype']
        try:
            obj=Login.objects.get(username=username,password=password)
            if obj is not None:
                if obj.usertype=='jobseeker':
                   request.session["username"]=username
                   return redirect("jsapp:jshome")
                elif obj.usertype=='administrator':
                    request.session["adminid"]=username
                    return redirect("adminapp:adminhome")
                elif obj.usertype=='employer':
                    request.session["username"]=username
                    return redirect("employer:employerhome")
        except ObjectDoesNotExist:
         return render(request,'login.html',{"msg":"Invalid user"}) 
    return render(request,"login.html")
def employerreg(request):
    if request.method=="POST":
        empprofilepic=request.POST["empprofilepic"]
        firmname=request.POST["firmname"]
        firmwork=request.POST["firmwork"]
        firmaddress=request.POST["firmaddress"]
        cpname=request.POST['cpname']
        cpcontactno=request.POST['cpcontactno']
        cpemailaddress=request.POST["cpemailaddress"]
        password=request.POST["password"]
        aadharno=request.POST["aadharno"]
        panno=request.POST["panno"]
        gstno=request.POST["gstno"]
        regdate=datetime.datetime.today()
        empreg=Employer(empprofilepic=empprofilepic,firmname=firmname,firmwork=firmwork,firmaddress=firmaddress,cpname=cpname,cpcontactno=cpcontactno,cpemailaddress=cpemailaddress,aadharno=aadharno,panno=panno,gstno=gstno,regdate=regdate)
        empreg.save()
        log=Login(username=cpemailaddress,password=password,usertype="employer")
        log.save()
        return render(request,"employer.html",{"msg":"Registration is done"})
    return render(request,"employer.html")
def contactus(request):
    if request.method=="POST": 
        name=request.POST["name"] 
        gender=request.POST["gender"]
        address=request.POST["address"]
        contactno=request.POST["contactno"]
        emailaddress=request.POST["emailaddress"]
        enquirytext=request.POST["enquirytext"]
        posteddate=datetime.datetime.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno, emailaddress=emailaddress, enquirytext=enquirytext, posteddate=posteddate)
        enq.save()
        return render(request,"contactus.html",{"msg":"Enquiry is saved"})
    return render(request,"contactus.html")
def apply(request):
    return render(request,"apply.html")
def services(request):
    return render(request,"services.html")
def blog(request):
        new=News.objects.all()
        return render(request,"blog.html",locals())


def update_application_status(request, app_id):
    application = get_object_or_404(Application, id=app_id)
    
    if request.method == 'POST':
        new_status = request.POST['status']
        application.status = new_status
        application.save()

        send_notification(
            "Application Status Update",
            f"Hi {application.applicant.first_name}, your application for '{application.job.title}' is now '{new_status}'.",
            application.applicant.email
        )

    return redirect('view_applications')

def post_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        job = Job.objects.create(title=title, category=category)

        # Find job seekers with matching preferred_category
        seekers = JobSeekerDetails.objects.filter(preferred_category=category)

        for seeker in seekers:
            send_notification(
                "New Job Matching Your Profile",
                f"Hi {seeker.user.first_name}, a new job '{title}' in category '{category}' was posted.",
                seeker.user.email
            )

        return redirect('job_list')

    return render(request, 'post_job.html')

def apply_job(request, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id)

        # Get the logged-in job seeker's email from session
        email = request.session.get("username")
        job_seeker = get_object_or_404(JobSeeker, emailaddress=email)

        # Create the application (avoid duplicates)
        application, created = Application.objects.get_or_create(
            user=job_seeker,
            job=job,
        )

        if created:
            # Send confirmation email
            send_mail(
                subject=f"Application Received for {job.title}",
                message=f"Hi {job_seeker.name},\n\nYou applied for '{job.title}' at {job.company}.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[job_seeker.emailaddress],
                fail_silently=False,
            )

            messages.success(request, "You have successfully applied for this job. Confirmation email sent.")
        else:
            messages.info(request, "You already applied for this job.")

        return redirect('job_list')  # or your job list page

    return redirect('job_list')