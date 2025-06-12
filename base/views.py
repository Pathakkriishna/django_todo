from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .models import Type
from .forms import TodoForm

# Create your views here.


def home(request):
    search = request.GET.get('search')
    if search != None and search != '':
        todos = Todo.objects.filter(name__contains = search)
        

    else:
        todos = Todo.objects.all()
    return render(request, 'index.html', context={'todos': todos})


def type(request):
    types = Type.objects.all()
    return render(request, 'type.html', context={'types': types})


def create_todo_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Todo.objects.create(name=name, description=description, status=status)

        return redirect('home')

    return render(request, 'create_todo.html')


def create_type_view(request):
    if request.method == 'POST':
        todo_type = request.POST.get('todo-type')

        Type.objects.create(name=todo_type)

    return render(request, 'create_type.html')


def update_todo_view(request, pk):

    todo_obj = Todo.objects.get(id=pk)
    todo_form = TodoForm(instance=todo_obj)
    if request.method == 'POST':
        todo_form = TodoForm(instance=todo_obj, data=request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('home')
    return render(request, 'update_todo.html', context={'form': todo_form})


def delete_todo_view(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('home')


