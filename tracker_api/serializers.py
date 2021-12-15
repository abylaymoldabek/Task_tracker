from rest_framework import serializers
from .models import Task, CheckList, ChangeStatus, Notification
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        def complete(self, task, new_status):
            if task.status != new_status:
                author = User.objects.get(id=self.context.get('request').user.id)
                ChangeStatus.objects.create(task=task, previous_status=task.status, current_status=new_status, author=author)
