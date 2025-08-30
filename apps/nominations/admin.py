from django.contrib import admin
from .models import Nomination

@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ("nominee_name", "nominator_name", "has_permission", "status", "date")
    list_filter = ("has_permission", "status", "date")
    search_fields = ("nominee_name", "nominator_name", "nominator_email")
