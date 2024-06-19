from django import forms
from .models import ProfileRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class ProfileRequestForm(forms.ModelForm):
    phone_number = forms.NumberInput()
    profile_picture = forms.ImageField(required=True)
    class Meta:
        model = ProfileRequest
        fields = ['phone_number','address','profile_picture']
        
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class UserUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']
        
    class Meta:
        model = User
        fields = ['username','email']
        

        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
        



