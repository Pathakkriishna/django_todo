from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .models import Type

# Create your views here.


def home(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', context={'todos': todos})


def type(request):
    types = Type.objects.all()
    return render(request, 'type.html', context={'types': types})
