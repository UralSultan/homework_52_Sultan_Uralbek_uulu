from django.shortcuts import render, redirect
from .models import Task, STATUS_CHOICES

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        Task.objects.create(
            description=request.POST.get('description', ''),
            status=request.POST.get('status', 'new'),
            due_date=request.POST.get('due_date') or None,
        )
        return redirect('task_list')

    return render(request, 'todo/task_form.html', {'status_choices': STATUS_CHOICES})