from django.db import models
# Create your models here.
class Jobs(models.Model):
    firmname=models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    jobdesc=models.TextField()
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=20)
    location=models.CharField(max_length=50)
    salarypa=models.IntegerField()
    posteddate=models.CharField(max_length=30)
    emailaddress=models.EmailField(max_length=50)
class Post(models.Model):
    cpname=models.TextField(max_length=300,default="")
    caption=models.TextField(max_length=500)
    media=models.FileField(upload_to="")
    posteddate=models.CharField(max_length=30,default="")