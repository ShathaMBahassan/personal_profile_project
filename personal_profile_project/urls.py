
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 
import aboutMe.views
import projects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/',include('aboutMe.urls')),
    path('projects/',include('projects.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
