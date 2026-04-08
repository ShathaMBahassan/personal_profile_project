from django.db import models
from aboutMe.models import aboutMe


# Create your models here.
class project(models.Model):
    name= models.CharField(max_length=200)
    association = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/')
    about_me = models.ForeignKey(aboutMe, on_delete=models.CASCADE)
    

    
