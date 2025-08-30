from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 6})}

    def save_and_notify(self):
        obj = self.save()
        try:
            send_mail(
                subject=f"[The Mom Network] {obj.subject}",
                message=f"From: {obj.name} <{obj.email}>\n\n{obj.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER] if settings.EMAIL_HOST_USER else ["admin@localhost"],
                fail_silently=True,
            )
        except Exception:
            pass
        return obj
