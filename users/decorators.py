from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import redirect
from functools import wraps
from django.contrib import messages



def is_admin(user):
    if user.groups.filter(name="Admin").exists():
        return True
    else:
        return False

def admin_required(view_func):
    login_url = reverse_lazy('login')
    decorated_view_func = user_passes_test(is_admin,login_url=login_url)
    return decorated_view_func(view_func)


def redirect_authenticated_user(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard') 
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def request_submission_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get('request_submitted'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('dashboard')  
    return _wrapped_view


