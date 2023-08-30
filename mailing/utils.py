from django.conf import settings
from django.core.mail import send_mail

from .models import EmailSchedule, MailingLog


def send_emails(pk: int) -> None:
    """
    Отправка писем.
    :param pk: id записи
    """
    obj = EmailSchedule.objects.get(pk=pk)
    emails = [client.email for client in obj.clients.all()]
    attempt = MailingLog.objects.create(
        settings=obj, status="failure", creator=obj.creator
    )
    try:
        send_mail(
            obj.message.subject,
            obj.message.body,
            settings.EMAIL_FROM,
            emails,
            fail_silently=False,
        )
    except Exception as e:
        attempt.response = repr(e)
    else:
        attempt.status = "success"
    finally:
        attempt.save()
