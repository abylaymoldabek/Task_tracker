from rest_framework import serializers
from .models import Task, CheckList, ChangeStatus, Notification
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
