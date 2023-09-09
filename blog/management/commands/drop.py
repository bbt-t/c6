from django.core.management import BaseCommand

from blog.models import BlogPost


class Command(BaseCommand):
    """
    Delete all data in DB.
    """

    def handle(self, *args, **options):
        BlogPost.objects.all().delete()
