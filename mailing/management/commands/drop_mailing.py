from django.core.management import BaseCommand


from mailing.models import Client, EmailSchedule, MailingLog, Message


class Command(BaseCommand):
    """
    Delete all data in DB.
    """

    def handle(self, *args, **options):
        Client.objects.all().delete()
        EmailSchedule.objects.all().delete()
        MailingLog.objects.all().delete()
        Message.objects.all().delete()
