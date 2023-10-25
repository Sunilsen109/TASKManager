from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user','task','task_desc','status']  # Use '__all__' to include all fields from the model
        widgets = {
       'user': forms.Select(attrs={'class':'form-control'}),
       'task': forms.TextInput(attrs={'class':'form-control'}),
       'task_desc': forms.TextInput(attrs={'class':'form-control'}),
       'status': forms.Select(attrs={'class':'form-control'}),
       
       
       } 