from django.shortcuts import render,redirect
from .decorators import admin_required
from .utils import is_admin
from .models import Project
from .forms import ProjectForm

# Create your views here.

@admin_required
def projects_list(request):
    projects = Project.objects.all()
    context = {
        "projects":projects
    }
    return render(request,'projects/projects_list.html',context)

def project_details(request,id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        if "update_project" in request.POST and is_admin(request.user):
            form = ProjectForm(request.POST,instance=project)
            if form.is_valid():
                form.save()
                return redirect('project_details',id)
        elif "delete_project" in request.POST and is_admin(request.user):
            project.delete()
            return redirect('dashboard')
    context = {
        'project':project,
        'form':ProjectForm(instance=project),
    }
    return render(request,'projects/project_details.html',context)

@admin_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})


