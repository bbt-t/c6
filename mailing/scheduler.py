from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


def start():
    scheduler.start()
