from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@shared_task
@periodic_task(run_every=crontab(minute=1))
def add(x, y):
    return x + y