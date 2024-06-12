from django.shortcuts import render
from django.http import JsonResponse
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.models import User


# Create your views here.

def project_status_data(request):
    projects_not_started = Project.objects.filter(status="Not Started").count()
    projects_in_progress = Project.objects.filter(status="In Progress").count()
    projects_completed = Project.objects.filter(status="Completed").count()

    data = {
        'labels': ['Not Started', 'In Progress', 'Completed'],
        'data': [projects_not_started, projects_in_progress, projects_completed],
        'backgroundColor': [
            'rgb(255, 99, 132)',  # Red for Not Started
            'rgb(54, 162, 235)',  # Blue for In Progress
            'rgb(75, 192, 192)'   # Green for Completed
        ]
    }
    return JsonResponse(data)


def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    users = User.objects.all()
    context = {
        'projects':projects.count(),
        'projects_in_progress':projects.filter(status="In Progress"),
        'tasks_number':tasks.count(),
        'important_tasks':tasks.filter(priority_level="High"),
        'users_number':users.count(),
    }
    return render(request,"dashboard/index.html",context)
