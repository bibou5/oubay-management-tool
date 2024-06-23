from django import forms
from .models import Notification

class CreateNotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message','reciptients']