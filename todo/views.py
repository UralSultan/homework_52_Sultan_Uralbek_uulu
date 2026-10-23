from django.shortcuts import render, redirect, get_object_or_404
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
            detail_descriptions=request.POST.get('details') or None,
        )
        return redirect('task_list')

    return render(request, 'todo/task_form.html', {'status_choices': STATUS_CHOICES})

def task_delete(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('task_list')