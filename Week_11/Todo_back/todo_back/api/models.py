from django.db import models
from datetime import datetime

class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False)
    due_on = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.name, self.created_at, self.due_on, self.status)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created at': self.created_at,
            'due on': self.due_on,
            'status': self.status
        }
