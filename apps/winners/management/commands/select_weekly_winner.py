from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from apps.entries.models import Entry
from apps.winners.models import WeeklyWinner

class Command(BaseCommand):
    help = "Select a weekly winner from entries and record it"

    def handle(self, *args, **kwargs):
        entries = list(Entry.objects.all())
        if not entries:
            self.stdout.write(self.style.WARNING("No entries found"))
            return
        winner = random.choice(entries)
        ww = WeeklyWinner.objects.create(
            name=winner.name,
            email=winner.email,
            date=timezone.now().date(),
            gift="Self-Care Package",
            notified=False,
        )
        self.stdout.write(self.style.SUCCESS(f"Winner selected: {ww.name} on {ww.date}"))
