from django.db import models
from django.contrib.auth.models import User

CHOICES = [(1, 'Planning'), (2, 'Active'), (3, 'Control'), (4, 'Finished')]


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    observer = models.ManyToManyField(to=User, related_name='observers')
    status = models.SmallIntegerField(choices=CHOICES, default=1)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'


class CheckList(models.Model):
    short_name = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.short_name} - {self.finished}'


class ChangeStatus(models.Model):
    CHOICES = [(1, 'Planning'), (2, 'Active'), (3, 'Control'), (4, 'Finished')]
    task = models.ForeignKey(Task, related_name='status_history', on_delete=models.CASCADE, )
    previous_status = models.SmallIntegerField(choices=CHOICES, default=1)
    current_status = models.SmallIntegerField(choices=CHOICES, default=1)
    author = models.ForeignKey(User, related_name='history_changes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task}'


class Notification(models.Model):
    task = models.ForeignKey(Task, related_name='nots', on_delete=models.CASCADE)
    text = models.TextField()
    recipients = models.ManyToManyField(User, related_name='recipients')

    def __str__(self):
        return f'{self.task} - {self.text}'
