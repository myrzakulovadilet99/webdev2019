from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from api.models import TaskList, Task

def t_lists(request):
    tasks = TaskList.objects.all()
    json_tasks = [t.to_json() for t in tasks]
    data = {
        'task list': json_tasks
    }
    return  JsonResponse(data, safe=False)

def task_lists_num(request, num):
    task = TaskList.objects.get(id = num).to_json()
    data = {
        'task': task
    }
    return JsonResponse(data, safe=False)

def task_lists_num_tasks(request, num):
    # return HttpResponse("<p>qwer</p>: {}".format(num))
    task_fromlist = TaskList.objects.get(id=num)
    tasks = task_fromlist.task_set.all()
    jsontask= [t.to_json() for t in tasks]
    data = {
        'task': jsontask
    }
    return JsonResponse(data, safe=False)

