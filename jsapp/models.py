from django.db import models
from jobapp.models import JobSeeker
from employer.models import Jobs  
# Create your models here.
class AppliedJobs(models.Model):
    id=models.AutoField(primary_key=True)
    empemailaddress=models.EmailField(max_length=50)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    dob=models.CharField(max_length=20)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    keyskills=models.TextField()
    applieddate=models.CharField(max_length=30)
class Response(models.Model):
    name=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    responsetype=models.CharField(max_length=50)
    subject=models.CharField(max_length=500)
    responsetext=models.CharField(max_length=5000)
    posteddate=models.CharField(max_length=30)
#  New Feature: Saved Job functionality
class SavedJob(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('jobseeker', 'job')  # Prevent duplicate saves

    def __str__(self):
        return f"{self.jobseeker.name} saved {self.job.jobtitle}"