from django.db import models

# Create your models here.
class aboutMe(models.Model):
    name = models.CharField(max_length=30)
    summary= models.CharField(max_length=500)
    email =models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    linked_in = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')

class Education(models.Model):
    degree=models.CharField(max_length=200)
    major=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    currentlly=models.BooleanField(default=False)
    date_start=models.DateField()
    date_end=models.DateField()
    about_me = models.ForeignKey(aboutMe,on_delete=models.CASCADE)
    

class certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField()
    date_start=models.DateField()
    date_end=models.DateField()
    about_me = models.ForeignKey(aboutMe,on_delete=models.CASCADE)

class experince(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    decription= models.TextField()   

class skills(models.Model):
    name = models.CharField(max_length=100)

class membership(models.Model):
    name= models.CharField(max_length=100)
    organization = models.CharField(max_length=100)

