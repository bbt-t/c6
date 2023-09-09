from django.apps import AppConfig
from django.conf import settings


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"
    verbose_name = "сервис управления рассылками"

    def ready(self):
        import mailing.signals
        from . import scheduler

        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
