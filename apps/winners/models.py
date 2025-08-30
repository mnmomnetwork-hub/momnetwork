from django.db import models

class WeeklyWinner(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField(blank=True)
    date = models.DateField()
    gift = models.CharField(max_length=160, blank=True)
    story = models.TextField(blank=True)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.date}"
