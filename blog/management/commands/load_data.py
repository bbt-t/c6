from pathlib import Path

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    """
    Load data to DB.
    """

    def handle(self, *args, **options):
        call_command(
            "loaddata",
            f"{Path(__file__).parent.parent.parent.parent}/data/blog_dump_data.json",
        )
