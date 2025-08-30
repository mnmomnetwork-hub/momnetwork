from django.db import models

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
]

class Story(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    story = models.TextField()
    wishlist_url = models.URLField(blank=True)
    allow_comments = models.BooleanField(default=False)
    share_publicly = models.BooleanField(default=False)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
