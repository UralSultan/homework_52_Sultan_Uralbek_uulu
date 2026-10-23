from django.shortcuts import render, get_object_or_404
from .models import Task, STATUS_CHOICES
from django.urls import reverse
from django.http import HttpResponseRedirect

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        task = Task.objects.create(
            description=request.POST.get('description', ''),
            status=request.POST.get('status', 'new'),
            due_date=request.POST.get('due_date') or None,
            detail_descriptions=request.POST.get('detail_descriptions') or None,
        )
        return HttpResponseRedirect(reverse('task_detail', kwargs={'task_id': task.pk}))
    return render(request, 'todo/task_form.html', {'status_choices': STATUS_CHOICES})

def task_delete(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return HttpResponseRedirect(reverse('task_list'))

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'todo/task_detail.html', {'task': task})