from django.shortcuts import render,redirect
from . models import Login,Employer,JobSeeker,Enquiry
from adminapp.models import News
from employer.models import Jobs
from django.core.exceptions import ObjectDoesNotExist
import datetime
# Create your views here.
def index(request):
    job=Jobs.objects.all()
    return render(request, "index.html", locals())
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
