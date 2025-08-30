from django.db import models

class Donation(models.Model):
    amount_cents = models.PositiveIntegerField()
    donor_email = models.EmailField(blank=True)
    donor_name = models.CharField(max_length=160, blank=True)
    status = models.CharField(max_length=20, default="created")  # created/completed/failed
    stripe_session_id = models.CharField(max_length=255, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def amount_dollars(self):
        return self.amount_cents / 100

    def __str__(self):
        return f"${self.amount_dollars:.2f} - {self.status}"
