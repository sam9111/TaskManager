from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

tasks = []


def tasks_view(request):
    return render(request, "tasks.html", {"tasks": tasks})


def add_task_view(
    request,
):
    task_value = request.GET.get("task")
    tasks.append(task_value)
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, index):
    del tasks[index - 1]
    return HttpResponseRedirect("/tasks")


def complete_task_view(request):
    pass


def completed_tasks_view(request):
    pass


def all_tasks_view(request):
    pass
