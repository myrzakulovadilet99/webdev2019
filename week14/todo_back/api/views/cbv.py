from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TasksSerializer2

class TaskListt(APIView):
    def get(self, request):
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskListNum(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_lists = self.get_object(pk)
        serializer = TaskListSerializer2(task_lists)
        return Response(serializer.data)

    def put(self, request, pk):
        task_lists = self.get_object(pk)
        serializer = TaskListSerializer2(instance=task_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_lists = self.get_object(pk)
        task_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskListNumTasks(APIView):
    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_lists = self.get_object(pk)
        tasks = task_lists.task_set.all()
        serializer = TasksSerializer2(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)