from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.

def tasks(request):
    return HttpResponse("welcome to dashboard")
