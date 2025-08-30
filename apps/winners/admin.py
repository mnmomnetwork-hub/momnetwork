from django.contrib import admin
from .models import WeeklyWinner

@admin.register(WeeklyWinner)
class WeeklyWinnerAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "gift", "notified")
    list_filter = ("date", "notified")
    search_fields = ("name", "email")
