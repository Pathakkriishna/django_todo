from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            "name" : forms.TextInput(attrs={'class': 'form-control'}),
            "description" : forms.Textarea(attrs={'class': 'form-control'}),
            "status" : forms.Select(attrs={'class': 'form-select'},choices = (('Done', 'Done'), ('Not Done', 'Not Done'), ('In Progress', 'In Progress'))),
        }
