import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RPG.settings')

app = Celery('RPG')

app.config_from_object('django.conf.settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_30_seconds': {
        'task': 'news.tasks.my_task',
        'schedule': 30,
        'args': (),
    },
}

app.autodiscover_tasks()