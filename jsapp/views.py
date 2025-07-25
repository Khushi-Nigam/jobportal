<<<<<<< HEAD
from django.shortcuts import render, redirect
from employer.models import Jobs, Post
from jsapp.models import Response, SavedJob
from django.contrib import messages
from jobapp.models import JobSeeker
from .models import AppliedJobs
from datetime import datetime
from jobapp.utils import send_notification_email

def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    return render(request, "contactus.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blog.html")

def login(request):
    return render(request, "login.html")

def employer(request):
    if request.method == "POST":
        companyname = request.POST.get("companyname")
        emailaddress = request.POST.get("emailaddress")
        password = request.POST.get("password")
        Employer(companyname=companyname, emailaddress=emailaddress, password=password).save()
        messages.success(request, "Employer account created successfully.")
        return redirect('login')
    return render(request, "employer.html")

def appliedjobs(request):
    if "username" not in request.session:
        return redirect("login")

    seeker_email = request.session["username"]
    jobs = AppliedJobs.objects.filter(emailaddress=seeker_email)

    return render(request, "appliedjobs.html", {"jobs": jobs})

def viewprofile(request):
    if "username" not in request.session:
        return redirect("login")

    seeker_email = request.session["username"]
    try:
<<<<<<< HEAD
        if request.session["username"]!=None:
            username=request.session["username"]
            user=JobSeeker.objects.get(emailaddress=request.session['username'])
            selected_tags = user.seeker_tags.all()
            recommended_posts = Jobs.objects.filter(job_tags__in=selected_tags)
=======
from django.shortcuts import render,redirect
from jobapp.models import JobSeeker,Employer
from django.views.decorators.cache import cache_control
from employer.models import Jobs,Post
import datetime
from . models import AppliedJobs,Response
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def jshome(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
>>>>>>> d0a70a6 (responsive-issue#27)
            empreg=Employer.objects.all()
            jobseek=JobSeeker.objects.get(emailaddress=username)
            job=Jobs.objects.all()
            apost=Post.objects.all()
            return render(request,"jshome.html",locals())
    except KeyError:
        return redirect("jobapp:login")
<<<<<<< HEAD
=======
        jobseeker = JobSeeker.objects.get(emailaddress=seeker_email)
    except JobSeeker.DoesNotExist:
        jobseeker = None

    return render(request, "viewprofile.html", {"jobseeker": jobseeker})

def response(request):
    if "username" not in request.session:
        return redirect("login")

    email = request.session["username"]
    responses = Response.objects.filter(emailaddress=email).order_by("-posteddate")

    return render(request, "response.html", {"responses": responses})

def jobseeker(request):
    if request.method == "POST":
        name = request.POST.get("name")
        emailaddress = request.POST.get("emailaddress")
        password = request.POST.get("password")
        Response(name=name, emailaddress=emailaddress, password=password).save()
        messages.success(request, "Job Seeker account created successfully.")
        return redirect('login')
    return render(request, "jobseeker.html")

def apply(request, jobid):
    if "username" not in request.session:
        return redirect("login")
    
    job = get_object_or_404(Jobs, id=jobid)
    
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        resume = request.FILES.get("resume")
        
        Response(job=job, fullname=fullname, email=email, phone=phone, resume=resume).save()
        messages.success(request, "Application submitted successfully.")
        return redirect("index")
    
    return render(request, "apply.html", {"job": job})

def parent(request):
    return render(request, "parent.html")

def admin_dashboard(request):
    jobs = Job.objects.all()
    return render(request, "admin.html", {"jobs": jobs})

def applyjob(request, jobid):
    if "username" not in request.session:
        return redirect("login")
    
    job = Job.objects.get(id=jobid)
    return render(request, "apply.html", {"job": job})

def myapplications(request):
    if "username" not in request.session:
        return redirect("login")
    
    email = request.session["username"]
    applications = Response.objects.filter(emailaddress=email)
    return render(request, "myapplications.html", {"applications": applications})

>>>>>>> upstream/master
def logout(request):
    try:
        del request.session["username"]
    except:
        pass
    return redirect("index")
def changepassword(request):
<<<<<<< HEAD
=======
def logout(request):
    try:
        del request.session["username"]
    except KeyError:
        return redirect("jobapp:login")
    return redirect("jobapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewjobs(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            jobseek=JobSeeker.objects.get(emailaddress=username)
            pjobs=Jobs.objects.all()
            return render(request,"viewjobs.html",locals())
    except KeyError:
        return redirect("jobapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewprofile(request):
    #try:
        if request.session["username"]!=None:
            username=request.session["username"]
            jobseek=JobSeeker.objects.get(emailaddress=username)
            if request.method=="POST":
                name=request.POST["name"]
                gender=request.POST["gender"]
                address=request.POST["address"]
                contactno=request.POST["contactno"]
                emailaddress=request.POST["emailaddress"]
                qualification=request.POST["qualification"]
                dob=request.POST["dob"]
                experience=request.POST["experience"]
                keyskills=request.POST["keyskills"]
                JobSeeker.object.all()
                return redirect("jsapp:jshome",locals())
            return render(request,"viewprofile.html",locals())
    #except KeyError:
        #return redirect("jobapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def changepassword(request):
>>>>>>> d0a70a6 (responsive-issue#27)
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            return render(request,"changepassword.html",locals())
    except KeyError:
        return redirect("jobapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def jsapply(request,id):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            job=Jobs.objects.get(id=id)
            jobseek=JobSeeker.objects.get(emailaddress=username)
            if request.method=="POST": 
                empemailaddress=request.POST["empemailaddress"] 
                jobtitle=request.POST["jobtitle"]
                post=request.POST['post'] 
                name=request.POST['name']
                gender=request.POST['gender']
                address=request.POST["address"]
                contactno=request.POST["contactno"]
                emailaddress=request.POST["emailaddress"]
                dob=request.POST["dob"]
                qualification=request.POST["qualification"]
                experience=request.POST["experience"]
                keyskills=request.POST["keyskills"]
                applieddate=datetime.datetime.today()
                app=AppliedJobs(empemailaddress=empemailaddress,jobtitle=jobtitle,post=post,name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,dob=dob,qualification=qualification,experience=experience,keyskills=keyskills,applieddate=applieddate)
                app.save()
                return render(request,"jsapply.html",{"msg":"Application is Submitted" , 'app':'app'})
            return render(request,"jsapply.html",{'job':job})
    except KeyError:
        return redirect("jobapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def appliedjobs(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            appl=AppliedJobs.objects.all()
            return render(request,"appliedjobs.html",locals())
    except KeyError:
        return redirect("jobapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def response(request):
    try:
        if request.session['username']!=None:
            jobseek=JobSeeker.objects.get(emailaddress=request.session["username"])
            if request.method=="POST":
                name = jobseek.name
                contactno = jobseek.contactno
                emailaddress = jobseek.emailaddress       
                responsetype = request.POST['responsetype']
                subject = request.POST['subject']
                responsetext=request.POST['responsetext']
                posteddate = datetime.datetime.today()
                res=Response(name=name,contactno=contactno,emailaddress=emailaddress,responsetype=responsetype,subject=subject,responsetext=responsetext,posteddate=posteddate)
                res.save()
                msg="Your response has been send successfully"
            return render(request,"response.html",locals())
        return render(request,"response.html")
    except KeyError:
        return redirect("jobapp:login")
<<<<<<< HEAD


   
=======
    if "username" not in request.session:
        return redirect("login")

    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        email = request.session["username"]

        try:
            user = Response.objects.get(emailaddress=email)

            if user.password != current_password:
                messages.error(request, "Current password is incorrect.")
                return redirect("changepassword")

            if new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
                return redirect("changepassword")

            user.password = new_password
            user.save()
            messages.success(request, "Password changed successfully.")
            return redirect("index")

        except Response.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect("login")

    return render(request, "changepassword.html")
# ✅ NEW FEATURE: Save Job
def savejob(request, jobid):
    if "username" not in request.session:
        return redirect("login")
    
    job = Job.objects.get(id=jobid)
    user_email = request.session["username"]

    # Check if already saved
    if not SavedJob.objects.filter(user_email=user_email, job=job).exists():
        SavedJob.objects.create(user_email=user_email, job=job)
        messages.success(request, "Job saved successfully.")
    else:
        messages.info(request, "You already saved this job.")
    
    return redirect("index")

def jsapply(request, id):
    if "username" not in request.session:
        return redirect("login")

    job = get_object_or_404(Jobs, id=id)
    seeker = get_object_or_404(JobSeeker, emailaddress=request.session['username'])

    if request.method == "POST":
        AppliedJobs.objects.create(
            empemailaddress=job.emailaddress,
            jobtitle=job.jobtitle,
            post=job.post,
            name=seeker.name,
            gender=seeker.gender,
            address=seeker.address,
            contactno=seeker.contactno,
            emailaddress=seeker.emailaddress,
            dob=seeker.dob,
            qualification=seeker.qualification,
            experience=seeker.experience,
            keyskills=seeker.keyskills,
            applieddate=datetime.now().strftime("%Y-%m-%d"),
        )
        # Send email notification to job seeker
        subject = "Application Received"
        message = f"Dear {seeker.name},\n\nYour application for {job.jobtitle} has been received."
        send_notification_email(subject, message, [seeker.emailaddress])
        return render(request, "applied_success.html", {"job": job})

    return render(request, "applyjob.html", {"job": job, "seeker": seeker})

def jshome(request):
    return render(request, 'jsapp/home.html')  # create jsapp/templates/jsapp/home.html if needed
def viewjobs(request):
    # Just rendering a template for now
    return render(request, 'jsapp/viewjobs.html')
>>>>>>> upstream/master
=======
>>>>>>> d0a70a6 (responsive-issue#27)
