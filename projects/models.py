from django.db import models


# Create your models here.
class project(models.Model):
    name= models.CharField(max_length=200)
    association = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField('/images')
    
    
