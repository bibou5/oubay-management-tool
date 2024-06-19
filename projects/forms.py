from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }