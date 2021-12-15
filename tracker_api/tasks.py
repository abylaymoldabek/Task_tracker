from django.conf import settings
from django.core.mail import send_mail as send_nudes
from .models import Task, Notification
from tracker.celery import app


@app.task
def send_mail(pk):
    task = Task.objects.get(id=pk)
    to_users = [observerq["email"] for observerq in task.observer.all().values("email")]
    send_nudes(pk, f"Hello, look task number #{task.id}. There is some updates", settings.EMAIL_HOST_USER, to_users)
    Notification.objects.create(task=task, text=f"Hello, look task number #{task.id}. There is some updates",
                                recipients=task.observer.all())
