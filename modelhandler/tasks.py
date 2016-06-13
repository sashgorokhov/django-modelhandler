import datetime

from celery import shared_task
from django.utils import timezone


@shared_task
def cleanup_logs(before=None):
    from modelhandler.models import Log
    before = before or timezone.now()
    return Log.objects.filter(created__lte=before).delete()


@shared_task
def cleanup_day():
    return cleanup_logs(timezone.now() - datetime.timedelta(days=1))


@shared_task
def cleanup_week():
    return cleanup_logs(timezone.now() - datetime.timedelta(days=7))


@shared_task
def cleanup_month():
    return cleanup_logs(timezone.now() - datetime.timedelta(days=30))
