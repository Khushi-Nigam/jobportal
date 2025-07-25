from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=50)
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.TextField(max_length=50)
    enquirytext=models.TextField()
    posteddate=models.CharField(max_length=30)
class JobSeeker(models.Model):
    profilepic=models.FileField(upload_to='',default="pic")
    name=models.CharField( max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50,primary_key=True)
    dob=models.CharField(max_length=20)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    keyskills=models.TextField()
    regdate=models.CharField(max_length=30)
class Employer(models.Model):
    empprofilepic=models.FileField(upload_to='',default="pic")
    firmname=models.CharField(max_length=100)
    firmwork=models.TextField()
    firmaddress=models.TextField()
    cpname=models.CharField(max_length=50)
    cpcontactno=models.CharField(max_length=15)
    cpemailaddress=models.EmailField(max_length=50,primary_key=True)
    aadharno=models.CharField(max_length=12)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=15)
    regdate=models.CharField(max_length=30)