from rest_framework import serializers
from .models import TaskList, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TasksSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    # task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list_id')

class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    tasks = TasksSerializer2(many=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'tasks')

    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        task_list = TaskList.objects.create(**validated_data)
        for task in tasks:
            Task.objects.create(task_list=task_list, **task)

        # arr = [Task(task_list=task_list, **task) for task in tasks]
        # Task.objects.bulk_create(arr)
        #
        # for i in range(0, len(arr), 100):
        #     # 0 100 200 300 400
        #     Task.objects.bulk_create(arr[i:i+100])

        return task_list