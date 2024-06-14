from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasks_list,name="tasks"),
    path('<int:id>/',views.task_details,name="task_details"),
    path('add/',views.add_task,name="add_task"),
]