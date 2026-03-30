from django.shortcuts import render
from .models import aboutMe , Education , certificate

# Create your views here.

def home(request):
    about_me = aboutMe.objects.all().first()
    edu = Education.objects.filter(about_me=1)
    cer = certificate.objects.filter(about_me=1)
    context={'about_me':about_me , 'edu':edu , 'cer':cer}
    return render(request, 'aboutMe\home.html',context)
