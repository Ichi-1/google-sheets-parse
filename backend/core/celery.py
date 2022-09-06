import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('test_app', broker='redis://redis:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# celery -A core worker -B -l INFO

app.conf.beat_schedule = {
    'parse-google-sheet-every-10-second': {
        'task': 'parse_google_sheet',
        'schedule': timedelta(seconds=10),
    },
    'notify_expired_supply-every-10-sec': {
        'task': 'notify_expired_supply',
        'schedule': timedelta(seconds=10)
    }
}