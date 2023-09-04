from smtplib import SMTPException

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
    log = MailingLog.objects.create(
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
    except SMTPException as err:
        log.response = repr(err)
    except Exception as err:
        print(repr(err))
    finally:
        log.save()
