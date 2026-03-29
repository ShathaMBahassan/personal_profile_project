from django.shortcuts import render
from .models import aboutMe

# Create your views here.

def home(request):
    about_me = aboutMe.objects.all().first()
    context={'about_me':about_me}
    return render(request, 'aboutMe\home.html',context)
