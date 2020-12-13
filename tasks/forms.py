from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add the new task here..'}))

    class Meta:
        model = Task
        field = '__all__'
        exclude = ()
