from api.serializers import TaskListSerializer2, TasksSerializer2,  UserSerializer
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django.http import Http404
from api.models import TaskList, Task
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import TaskFilter

class TaskListt(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

class TaskListNum(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


class TaskListNumTasks(generics.ListCreateAPIView):
    serializer_class = TasksSerializer2
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)


    # TODO DjangoFilterBackend
    filter_class = TaskFilter
    # filterset_fields = ('name', 'status')

    # TODO SearchFilter
    search_fields = ('name', 'status', 'created_at', 'due_on')

    # TODO OrderingFilter
    ordering_fields = ('name', 'status')
    ordering = ('status',)

    def get_queryset(self):
        # task_list=get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        try:
            task_list = TaskList.objects.get(id=self.kwargs.get('pk'))
        except TaskList.DoesNotExist:
            raise Http404
        queryset = task_list.tasks.all()

        # TODO Query params
        # name = self.request.query_params.get('name', None)
        # status = self.request.query_params.get('status', None)
        # if name is not None and status is not None:
        #     queryset = queryset.filter(name=name).filter(status=status)

        return queryset