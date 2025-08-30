from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "email", "status", "share_publicly", "created_at")
    list_filter = ("status", "share_publicly", "created_at")
    search_fields = ("title", "name", "email")
