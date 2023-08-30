from pathlib import Path

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    """
    Dump data from DB.
    """

    def handle(self, *args, **options):
        call_command(
            "dumpdata",
            f"{Path(__file__).parent.parent.parent.parent}/data/blog_dump_data.json",
        )
