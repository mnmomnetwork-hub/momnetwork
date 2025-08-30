from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    subject = models.CharField(max_length=160)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, default="new")

    def __str__(self):
        return f"{self.subject} from {self.name}"
