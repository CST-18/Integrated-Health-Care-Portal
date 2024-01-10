from django.db import models
from django.contrib.auth.models import User


class Apps(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phoneNo = models.CharField(max_length=15)
    appointment = models.CharField(max_length=255)
    symptoms = models.TextField()
    is_approved = models.BooleanField(default=False)

class Contact(models.Model):
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    add=models.TextField()

class Patient(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    # marital_status = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=10)
    aadharnumber = models.CharField(max_length=12)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    address = models.TextField()
    symptoms = models.TextField()
    # Emergency Details
    ename = models.CharField(max_length=30)
    relation = models.CharField(max_length=30)  
    emergencynumber = models.CharField(max_length=10)

# Create your models here.

# models.py

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_data = models.TextField()

    def __str__(self):
        return self.user.username
    
class Doctor(models.Model):
    dname = models.CharField(max_length=10)
    specialization = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)


