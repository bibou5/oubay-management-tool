from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects_list,name="projects"),
    path('<slug:slug>/',views.project_details,name="project_details"),
    path('add/',views.add_project,name="add_project"),
]