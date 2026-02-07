from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    tasks = Task.objects.all()
    return render(request,'home.html',{'tasks':tasks})



def toggle_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("/")



def add_task(request):   
    if request.method == 'POST':       
        title = request.POST.get('title')
        if title:           
            Task.objects.create(title=title)
    return redirect('home')


def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('home')


def edit_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
            task.save()
            return redirect('home')
    return render(request,'edit.html',{'task':task})