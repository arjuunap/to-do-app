from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, "home.html", {"tasks": tasks})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("/")
