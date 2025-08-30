from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "agree_to_rules", "created_at")
    search_fields = ("name", "email")
    list_filter = ("agree_to_rules", "created_at")
