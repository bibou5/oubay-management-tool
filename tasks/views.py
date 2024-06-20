from django.shortcuts import render,redirect
from .decorators import admin_required,is_admin

from .models import Task
from .forms import TaskForm

# Create your views here.

@admin_required
def tasks_list(request):
    tasks = Task.objects.all()
    context = {
        "tasks":tasks
    }
    return render(request,'tasks/tasks_list.html',context)

def task_details(request,slug):
    task = Task.objects.get(slug=slug)
    if request.method == "POST":
        if "update_task" in request.POST and is_admin(request.user):
            form = TaskForm(request.POST,instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_details',slug)
        elif "delete_task" in request.POST and is_admin(request.user):
            task.delete()
            return redirect('dashboard')
    context = {
        'task':task,
        'form':TaskForm(instance=task),
    }
    return render(request,'tasks/task_details.html',context)

@admin_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})
