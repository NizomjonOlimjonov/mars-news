from django.shortcuts import render, HttpResponse
from .models import Task
# Create your views here.


def main_page(request):
    tasks = Task.objects.all()

    return render(request, 'index.html', context={'tasks': tasks})


def about_page(request):
    tasks = Task.objects.all()

    return render(request, 'about.html', context={'tasks': tasks})




