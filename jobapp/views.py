from django.shortcuts import render,redirect
from .models import Login,Employer,JobSeeker,Enquiry
from adminapp.models import News
from employer.models import Jobs
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    jobs = Jobs.objects.all()

    location = request.GET.get('location')
    experience = request.GET.get('experience')

    if location:
        jobs = jobs.filter(location__icontains=location)

    if experience:
        jobs = jobs.filter(experience__icontains=experience)

    return render(request, "index.html", {'jobs': jobs, 'location': location, 'experience': experience})

def aboutus(request):
    return render(request,"aboutus.html")
def jobseekerreg(request):
    if request.method == "POST":
        profilepic = request.POST["profilepic"]
        name = request.POST["name"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        contactno = request.POST["contactno"]
        emailaddress = request.POST["emailaddress"]
        password = request.POST["password"]
        dob = request.POST["dob"]
        regdate = datetime.datetime.today()

        jobseek = JobSeeker(
            profilepic=profilepic,
            name=name,
            gender=gender,
            address=address,
            contactno=contactno,
            emailaddress=emailaddress,
            dob=dob,
            regdate=regdate
        )
        jobseek.save()

        log = Login(username=emailaddress, password=password, usertype="jobseeker")
        log.save()

        messages.success(request, "Registration successful! You can now log in.")
        return render(request, "jobseeker.html", {"show_modal": True})

    return render(request, "jobseeker.html")

def login(request):
    if request.method=="POST":  
        username=request.POST["username"]
        password=request.POST["password"]
        # usertype=request.POST['usertype']
        try:
            obj = Login.objects.get(username=username, password=password)
            usertype = obj.usertype 
            request.session["username"] = username
            request.session["usertype"] = usertype
            if usertype == 'jobseeker':
                request.session["usertype"] = usertype
                return redirect("jsapp:jshome")
            elif usertype == 'administrator':
                request.session["adminid"] = username
                return redirect("adminapp:adminhome")
            elif usertype == 'employer':
                request.session["usertype"] = usertype
                return redirect("employer:employerhome")
            else:
                return render(request, 'login.html', {"msg": "Invalid user type"})
        except ObjectDoesNotExist:
         return render(request,'login.html',{"msg":"Invalid user"}) 
    return render(request,"login.html")
def employerreg(request):
    if request.method == "POST":
        empprofilepic = request.FILES.get("empprofilepic")
        firmname = request.POST["firmname"]
        firmwork = request.POST["firmwork"]
        firmaddress = request.POST["firmaddress"]
        cpname = request.POST["cpname"]
        cpcontactno = request.POST["cpcontactno"]
        cpemailaddress = request.POST["cpemailaddress"]
        password = request.POST["password"]
        aadharno = request.POST["aadharno"]
        panno = request.POST["panno"]
        gstno = request.POST["gstno"]
        regdate = datetime.datetime.today()

        empreg = Employer(
            empprofilepic=empprofilepic,
            firmname=firmname,
            firmwork=firmwork,
            firmaddress=firmaddress,
            cpname=cpname,
            cpcontactno=cpcontactno,
            cpemailaddress=cpemailaddress,
            aadharno=aadharno,
            panno=panno,
            gstno=gstno,
            regdate=regdate
        )
        empreg.save()

        log = Login(username=cpemailaddress, password=password, usertype="employer")
        log.save()

        messages.success(request, "Employer registration successful! Please log in.")
        return render(request, "employer.html", {"show_modal": True})

    return render(request, "employer.html")

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
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Login.objects.get(username=email)
            # For now, just show a success message (simulate email sent)
            return render(request, 'reset_password.html', {'user_email': user.username})
        except Login.DoesNotExist:
            messages.error(request, "Email not registered.")
    return render(request, 'forgot_password.html')