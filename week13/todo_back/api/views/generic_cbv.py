from api.models import TaskList
from django.contrib.auth.models import User
from api.serializers import TaskListSerializer2, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class task_list(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    #
    # def get_serializer_class(self):
    #     return TaskListSerializer2


class task_lists_num(generics.RetrieveUpdateDestroyAPIView):
    # queryset = TaskList.objects.all()
    # serializer_class = TaskListSerializer2

    def get_queryset(self):
        return TaskList.objects.all()
    def get_serializer_class(self):
        return TaskListSerializer2
