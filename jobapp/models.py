from django.db import models

# Avoid storing passwords in plain text!
# If you're not using Django's built-in auth system, hash passwords before saving!

class Login(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=128)  # Increased length for hashed passwords
    usertype = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.CharField(max_length=100)  # TextField doesn't support max_length, use CharField
    contactno = models.CharField(max_length=15)
    emailaddress = models.EmailField(max_length=50)
    enquirytext = models.TextField()
    posteddate = models.DateField()  # Prefer DateField for dates

    def __str__(self):
        return f"{self.name} - {self.emailaddress}"


class JobSeeker(models.Model):
    profilepic = models.ImageField(upload_to='jobseekers/', default='pic')  # FileField -> ImageField + folder
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.TextField()
    contactno = models.CharField(max_length=15)
    emailaddress = models.EmailField(max_length=50, primary_key=True)
    dob = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=20)
    keyskills = models.TextField()
    regdate = models.DateField()

    def __str__(self):
        return self.emailaddress


class Employer(models.Model):
    empprofilepic = models.ImageField(upload_to='employers/', default='pic')
    firmname = models.CharField(max_length=100)
    firmwork = models.TextField()
    firmaddress = models.TextField()
    cpname = models.CharField(max_length=50)
    cpcontactno = models.CharField(max_length=15)
    cpemailaddress = models.EmailField(max_length=50, primary_key=True)
    aadharno = models.CharField(max_length=12)
    panno = models.CharField(max_length=10)
    gstno = models.CharField(max_length=15)
    regdate = models.DateField()

    def __str__(self):
        return self.firmname
