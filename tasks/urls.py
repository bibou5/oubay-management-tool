from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasks_list,name="tasks"),
    path('add/',views.add_task,name="add_task"),
    path('<slug:slug>/',views.task_details,name="task_details"),
    
]