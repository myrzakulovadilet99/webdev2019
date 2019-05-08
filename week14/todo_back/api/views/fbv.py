from ..models import TaskList, Task
from api.serializers import TaskListSerializer2, TasksSerializer2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'PUT', 'DELETE'])
def task_lists_num(request, pk):
    try:
        task_lists = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer2(task_lists)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer2(instance=task_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        task_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def task_lists_num_tasks(request, pk):
    try:
        task_lists = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tasks = task_lists.task_set.all()
    serializer = TasksSerializer2(tasks,many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)