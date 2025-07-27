from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from employer.models import Jobs, Post
from jsapp.models import Response, SavedJob
from django.contrib import messages
from jobapp.models import JobSeeker
from .models import *
from datetime import datetime
from jobapp.utils import send_notification_email
from django.shortcuts import render
import os
from groq import Groq  
import requests
from dotenv import load_dotenv
load_dotenv()
# Initialize Groq client

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


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
        jobseeker = JobSeeker.objects.get(emailaddress=seeker_email)
    except JobSeeker.DoesNotExist:
        return redirect("login") 

    if request.method == "POST":
        jobseeker.name = request.POST.get("name")
        jobseeker.address = request.POST.get("address")
        jobseeker.contactno = request.POST.get("contactno")
        jobseeker.emailaddress = request.POST.get("emailaddress")
        jobseeker.qualification = request.POST.get("qualification")
        jobseeker.dob = request.POST.get("dob")
        jobseeker.experience = request.POST.get("experience")
        jobseeker.keyskills = request.POST.get("keyskills")
        jobseeker.save()
        return render(request, 'viewprofile.html', {"jobseeker": jobseeker})

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
    jobs = Jobs.objects.all()
    return render(request, "admin.html", {"jobs": jobs})

def applyjob(request, jobid):
    if "username" not in request.session:
        return redirect("login")
    
    job = Jobs.objects.get(id=jobid)
    job = Jobs.objects.get(id=jobid)
    return render(request, "apply.html", {"job": job})

def myapplications(request):
    if "username" not in request.session:
        return redirect("login")
    
    email = request.session["username"]
    applications = Response.objects.filter(emailaddress=email)
    return render(request, "myapplications.html", {"applications": applications})

def logout(request):
    try:
        del request.session["username"]
    except:
        pass
    return redirect("index")
def changepassword(request):
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
# NEW FEATURE: Save Job
def savejob(request, jobid):
    if "username" not in request.session:
        return redirect("login")
    
    job = Jobs.objects.get(id=jobid)
    job = Jobs.objects.get(id=jobid)
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
        already_applied = AppliedJobs.objects.filter(emailaddress=seeker.emailaddress, jobtitle=job.jobtitle).exists()
        if already_applied:
            return HttpResponse("You have already applied for this job.")
        
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
        # subject = "Application Received"
        # message = f"Dear {seeker.name},\n\nYour application for {job.jobtitle} has been received."
        # send_notification_email(subject, message, [seeker.emailaddress])
        all_applied_jobs = AppliedJobs.objects.filter(emailaddress=seeker.emailaddress)
        return render(request, "appliedjobs.html", {"jobs": all_applied_jobs})

    return render(request, "jsapply.html", {"job": job, "seeker": seeker})

def jshome(request):
    return render(request, 'jshome.html')  # create jsapp/templates/jsapp/home.html if needed
def viewjobs(request):
    all_jobs = Jobs.objects.all()
    # Just rendering a template for now
    return render(request, 'viewjobs.html', context={'pjobs' : all_jobs})

def extract_ids_from_response(text):
    # Tries to extract job IDs from LLM response
    import re
    return list(map(int, re.findall(r'\d+', text)))  # crude but effective

def job_search(request):
    user_query = request.GET.get("q", "")
    if not user_query:
        return render(request, "jshome.html", {"suggestions": []})

    # Fetch all jobs (limit to 50 for performance)
    all_jobs = Jobs.objects.all()[:50]
    job_data = [
        {
            "id": job.id,
            "title": job.jobtitle,
            "desc": job.jobdesc,
            "firm": job.firmname,
            "post": job.post,
            "location": job.location,
            "qual": job.qualification,
            "experience": job.experience,
        }
        for job in all_jobs
    ]

    # Construct prompt for LLM
    prompt = f"""
You are an intelligent job search assistant. A user is looking for jobs based on this query:

"{user_query}"

Here are the available jobs (each with id, title, description, etc.):

{job_data}

From this list, return the IDs of the jobs that best match the query — even if the wording is not exactly the same. Use your understanding of context and synonyms.

Respond with a Python-style list of IDs, like: [2, 8, 19]
"""

    try:
        # Call Groq LLM API
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
            json={
                "model": "llama3-70b-8192",  # or "llama3-70b-8192"
                "messages": [
                    {"role": "system", "content": "You are a helpful AI job recommender."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.2,
            },
            timeout=10
        )

        # Extract job IDs from LLM response
        llm_response = response.json()
        raw_text = llm_response["choices"][0]["message"]["content"]
        matched_ids = extract_ids_from_response(raw_text)

        matched_jobs = Jobs.objects.filter(id__in=matched_ids)

    except Exception as e:
        print("LLM Search Error:", e)
        matched_jobs = []

    return render(request, "jshome.html", {
        "query": user_query,
        "suggestions": matched_jobs,
    })
