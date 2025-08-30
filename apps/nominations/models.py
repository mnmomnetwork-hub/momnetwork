from django.db import models

class Nomination(models.Model):
    nominee_name = models.CharField(max_length=160)
    nominee_location = models.CharField(max_length=160)
    nominator_name = models.CharField(max_length=160)
    nominator_email = models.EmailField()
    reason = models.TextField(blank=True)
    has_permission = models.BooleanField(default=False)
    status = models.CharField(max_length=16, default="pending")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nominee_name} nominated by {self.nominator_name}"
