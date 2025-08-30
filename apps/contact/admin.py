from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "status", "date")
    list_filter = ("status", "date")
    search_fields = ("subject", "name", "email")
