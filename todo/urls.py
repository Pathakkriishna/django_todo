"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import home, type, create_todo_view, create_type_view, update_todo_view, delete_todo_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('type/', type, name = 'type'),
    path('create/todo/', create_todo_view, name = 'create-todo'),
    path('create/type/', create_type_view, name = 'create-type'),
    path('update/todo/<int:pk>/', update_todo_view, name = 'update-todo'),
    path('delete/todo/<int:pk>/', delete_todo_view, name = 'delete-todo'),
]
