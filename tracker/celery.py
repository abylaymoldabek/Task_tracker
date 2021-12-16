import os

from celery import Celery
from celery.schedules import crontab
from tracker_api.models import Task
from tracker_api import tasks

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracker.settings')

app = Celery('tracker')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-me-every-commit": {
        "task": "tracker.tasks.my_task",
        "schedule": crontab()
    }
}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    task = Task.objects.all()
    sender.add_periodic_task(
        crontab(hour=1),
        tasks.task_shad(task.pk),
    )
