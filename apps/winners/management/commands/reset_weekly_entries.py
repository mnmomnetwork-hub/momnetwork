from django.core.management.base import BaseCommand
from apps.entries.models import Entry

class Command(BaseCommand):
    help = "Reset weekly entries (clears all entries)"

    def handle(self, *args, **kwargs):
        count, _ = Entry.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {count} entries"))
