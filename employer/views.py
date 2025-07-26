from django.shortcuts import render,redirect
from jobapp.models import Employer,JobSeeker
from . models import Jobs,Post
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.core.exceptions import PermissionDenied
import datetime
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from jobapp.models import Employer, JobSeeker
from .models import Jobs, Post
from jsapp.models import AppliedJobs
# Create your views here.

from jobapp.utils import send_notification_email


def employer_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if "username" not in request.session:
            return redirect("jobapp:login")
        try:
            employer = Employer.objects.get(cpemailaddress=request.session["username"])
            return view_func(request, *args, **kwargs)
        except Employer.DoesNotExist:
            messages.error(request, "Invalid employer account")
            return redirect("jobapp:login")
    return wrapper

@employer_login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def employerhome(request):
    username = request.session["username"]
    empreg = Employer.objects.get(cpemailaddress=username)
    return render(request, "employerhome.html", locals())


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    if "username" in request.session:
        del request.session["username"]
    return redirect("jobapp:login")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@employer_login_required
def jobs(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            empreg=Employer.objects.get(cpemailaddress=username)
            if request.method=="POST":
                firmname=request.POST['firmname']
                jobtitle=request.POST['jobtitle']
                post=request.POST['post']
                jobdesc=request.POST['jobdesc']
                qualification=request.POST['qualification']
                experience=request.POST['experience']
                location=request.POST['location']
                salarypa=request.POST['salarypa']
                posteddate=datetime.datetime.today()
                emailaddress=request.POST['emailaddress']
                pjobs=Jobs(firmname=firmname,jobtitle=jobtitle,post=post,jobdesc=jobdesc,qualification=qualification,experience=experience,location=location,salarypa=salarypa,posteddate=posteddate,emailaddress=emailaddress)
                pjobs.save()
                msg="Job Post is added"
                return render(request,"jobs.html",locals())
            return render(request,"jobs.html",locals())
    except KeyError:
        return redirect("jobapp:login")
    username = request.session["username"]
    empreg = Employer.objects.get(cpemailaddress=username)
    
    if request.method == "POST":
        try:
            firmname = request.POST['firmname']
            jobtitle = request.POST['jobtitle']
            post = request.POST['post']
            jobdesc = request.POST['jobdesc']
            qualification = request.POST['qualification']
            experience = request.POST['experience']
            location = request.POST['location']
            salarypa = request.POST['salarypa']
            tags = request.POST.get('tagname', '')
            posteddate = datetime.datetime.today()
            emailaddress = request.POST['emailaddress']

            # Validate Email Matches Logged in Employer
            if emailaddress != username:
                raise PermissionDenied("Email doesn't match logged in employer")

            pjobs = Jobs(
                firmname=firmname, jobtitle=jobtitle, post=post,
                jobdesc=jobdesc, qualification=qualification,
                experience=experience, location=location,
                salarypa=salarypa, posteddate=posteddate,
                emailaddress=emailaddress
            )
            pjobs.save()


            # Send Notifications To Matching Job Seekers
            matching_seekers = JobSeeker.objects.filter(
                qualification__icontains=qualification
            )
            emails = [seeker.emailaddress for seeker in matching_seekers if seeker.emailaddress]
            
            if emails:
                subject = "New Job Matching Your Profile"
                message = f"Dear Job Seeker,\n\nA new job '{jobtitle}' matching your profile has been posted. Log in to apply!"
                send_notification_email(subject, message, emails)

            messages.success(request, "Job Post added successfully")
            return redirect("employer:postedjobs")

        except Exception as e:
            messages.error(request, f"Error creating job: {str(e)}")
    
    return render(request, "jobs.html", locals())


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@employer_login_required
def postedjobs(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            pjobs=Jobs.objects.filter(emailaddress=username)
            emp=Employer.objects.all()
        return render(request,"postedjobs.html",locals())
    except KeyError:
        return redirect("jobapp:login")
def deljob(request,post):
    Jobs.objects.get(post=post).delete()
    return redirect("employer:postedjobs")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def discussion(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            return render(request,"discussion.html",locals())
    except KeyError:
        return redirect("employer:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewapplicants(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            post=AppliedJobs.objects.filter(emailaddress=username)
            return render(request,"viewapplicants.html",locals())
    except KeyError:
        return redirect("jobapp:login")
def reject(request,emailaddress):
    AppliedJobs.objects.get(emailaddress=emailaddress).delete()
    return redirect("employer:viewapplicants")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewmyprofile(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            empreg=Employer.objects.get(cpemailaddress=username)
            if request.method=="POST":
                firmname=request.POST["firmname"]
                firmwork=request.POST["firmwork"]
                firmaddress=request.POST["firmaddress"]
                cpname=request.POST["cpname"]
                cpcontactno=request.POST["cpcontactno"]
                cpemailaddress=request.POST["cpemailaddress"]
                Employer.objects.all(cpemailaddress=cpemailaddress).update(firmname=firmname,firmwork=firmwork,firmaddress=firmaddress,cpname=cpname,cpcontactno=cpcontactno)
                return redirect("employer:employerhome",locals())
            return render(request,"viewmyprofile.html",locals())
    except KeyError:
        return redirect("jobapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def addpost(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            empreg=Employer.objects.get(cpemailaddress=username)
            if request.method=="POST":
                cpname=request.POST['cpname']
                cpemailaddress=request.POST['cpemailaddress']
                caption=request.POST['caption']
                media=request.FILES['media']
                posteddate=datetime.datetime.today()
                apost=Post(cpname=cpname,cpemailaddress=cpemailaddress,caption=caption,media=media,posteddate=posteddate)
                apost.save()
                msg="Post is added"
                return render(request,"addpost.html",locals())
            return render(request,"addpost.html",locals())
    except KeyError:
        return redirect("jobapp:login")
    username = request.session["username"]
    pjobs = Jobs.objects.filter(emailaddress=username)
    return render(request, "postedjobs.html", {"pjobs": pjobs})


@employer_login_required
def deljob(request, pk):
    job = get_object_or_404(Jobs, pk=pk, emailaddress=request.session["username"])
    job.delete()
    messages.success(request, "Job deleted successfully")
    return redirect("employer:postedjobs")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@employer_login_required
def discussion(request):
    return render(request, "discussion.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@employer_login_required
def viewapplicants(request):
    username = request.session["username"]
    applicants = AppliedJobs.objects.filter(job__emailaddress=username)
    return render(request, "viewapplicants.html", {"applicants": applicants})


@employer_login_required
def reject(request, pk):
    application = get_object_or_404(
        AppliedJobs,
        pk=pk,
        job__emailaddress=request.session["username"]
    )
    
    # Send Rejection Email
    subject = "Application Status Update"
    message = (
        f"Dear {application.name},\n\n"
        f"We regret to inform you that your application for "
        f"{application.job.jobtitle} has been rejected."
    )
    send_notification_email(subject, message, [application.emailaddress])
    
    application.delete()
    messages.success(request, "Application rejected and notification sent")
    return redirect("employer:viewapplicants")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@employer_login_required
def viewmyprofile(request):
    username = request.session["username"]
    empreg = get_object_or_404(Employer, cpemailaddress=username)
    
    if request.method == "POST":
        try:
            empreg.firmname = request.POST["firmname"]
            empreg.firmwork = request.POST["firmwork"]
            empreg.firmaddress = request.POST["firmaddress"]
            empreg.cpname = request.POST["cpname"]
            empreg.cpcontactno = request.POST["cpcontactno"]
            empreg.save()
            messages.success(request, "Profile updated successfully")
            return redirect("employer:employerhome")
        except Exception as e:
            messages.error(request, f"Error updating profile: {str(e)}")
    
    return render(request, "viewmyprofile.html", {"empreg": empreg})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@employer_login_required
def addpost(request):
    username = request.session["username"]
    empreg = get_object_or_404(Employer, cpemailaddress=username)
    
    if request.method == "POST":
        try:
            caption = request.POST['caption']
            media = request.FILES.get('media')
            
            if not media:
                raise ValueError("Media file is required")
            
            apost = Post(
                cpname=empreg.cpname,
                cpemailaddress=username,
                caption=caption,
                media=media,
                posteddate=datetime.datetime.today()
            )
            apost.save()
            messages.success(request, "Post added successfully")
            return redirect("employer:employerhome")
        
        except Exception as e:
            messages.error(request, f"Error creating post: {str(e)}")
    
    return render(request, "addpost.html", {"empreg": empreg})