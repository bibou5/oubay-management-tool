from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import ProfileRequest
from .decorators import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@redirect_authenticated_user
def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileRequestForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            phone_number = request.POST['phone_number']
            address = request.POST['address']
            profile_picture = request.FILES['profile_picture']
            ProfileRequest.objects.create(user=user, phone_number=phone_number, address=address, profile_picture=profile_picture,is_approved=False)
            request.session['request_submitted'] = True
            return redirect('request_success')
    else:
        user_form = UserForm()
        profile_form = ProfileRequestForm()
    return render(request,'registration/signup.html',{'user_form':user_form,"profile_form":profile_form})


def sucess_page(request):
    if request.session.get('request_submitted',False):
        del request.session['request_submitted']
        return render(request,'registration/request_success.html')
    else:
        return redirect('signup')

@admin_required
def profile_requests_list(request):
    if request.method == "POST":
        request_id = request.POST['request_id']
        profile_request = ProfileRequest.objects.get(id=request_id)
        if 'approve' in request.POST:
            profile_request.is_approved = True
            profile_request.save()
        elif 'reject' in request.POST:
            user = profile_request.user
            if user:
                user.delete()
            
        return redirect('profile_requests_list')
    else:
        requests = ProfileRequest.objects.filter(is_approved=False)
    return render(request,'registration/profile_requests_list.html',{'requests':requests})

from django.contrib import messages

@redirect_authenticated_user
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                profile_request = ProfileRequest.objects.get(user=user)
                if profile_request.is_approved:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Your account has not been approved yet.')
            else:
                messages.error(request, 'Invalid username or password or you request has been rejected')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    request.session['logged_out'] = True
    return redirect('logged_out')

def logged_out(request):
    if request.session.get('logged_out',False):
        del request.session['logged_out']
        return render(request, 'registration/logged_out.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def profile(request):
    profile = ProfileRequest.objects.get(user=request.user)
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileRequestForm(request.POST,request.FILES,instance=profile)
        if user_update_form.is_valid() and profile_form.is_valid():
            user_update_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileRequestForm(instance=profile)
    return render(request, 'accounts/profile.html',{'profile':profile,'user_update_form':user_update_form,"profile_form":profile_form}) 

@admin_required
def profiles_list(request):
    profiles = ProfileRequest.objects.filter(is_approved=True)
    return render(request,'accounts/profiles_list.html',{'profiles':profiles})

@admin_required
def profile_details(request,slug):
    profile = ProfileRequest.objects.get(slug=slug)
    return render(request,'accounts/profile_details.html',{'profile':profile})

@admin_required
def delete_profile(request,slug):
    profile = ProfileRequest.objects.get(slug=slug)
    user = profile.user
    if request.method == "POST":
        user.delete()
        return redirect('profiles_list')
    return render(request,'accounts/delete_profile_confirmation.html')



