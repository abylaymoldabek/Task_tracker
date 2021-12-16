from django.conf import settings
from django.core.mail import send_mail as send_nudes
from .models import Task, Notification
from tracker.celery import app
from datetime import datetime
from text_notification import text_not


def mail_notification(text, task, pk):
    to_users = [observerq["email"] for observerq in task.observer.all().values("email")]
    send_nudes(pk, text, settings.EMAIL_HOST_USER,
               to_users)
    Notification.objects.create(task=task,
                                text=text,
                                recipients=task.observer.all())


@app.task
def send_mail(pk):
    task = Task.objects.get(id=pk)
    to_users = [observerq["email"] for observerq in task.observer.all().values("email")]
    send_nudes(pk, f"Hello, look task number #{task.id}. There is some updates", settings.EMAIL_HOST_USER, to_users)
    Notification.objects.create(task=task, text=f"Hello, look task number #{task.id}. There is some updates",
                                recipients=task.observer.all())


@app.task
def task_shad(pk):
    task = Task.objects.get(id=pk)
    if task.start_time > datetime.now():
        mail_notification(text_not(task).planning, task, pk)
    elif task.start_time <= datetime.now() < task.end_time:
        if not task.status == 'active':
            mail_notification(text_not(task).active, task, pk)
            task.status = 'active'
            task.save()
    elif datetime.now() >= task.end_time:
        mail_notification(text_not(task).finished, task, pk)
