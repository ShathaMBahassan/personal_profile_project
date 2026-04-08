from django.shortcuts import render
from .models import project 

# Create your views here.

def projcet(request):
    pro = project.objects.filter(about_me=1)
    for i in pro:
        i.description = i.description.replace('●','<br>●')
    return render(request,'project\project.html', {'project':pro})
