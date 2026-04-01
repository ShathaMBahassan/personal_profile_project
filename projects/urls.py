from django.urls import path 
from . import views 


urlpatterns = [
    path('project_details/', views.projcet ,name="project")
]

