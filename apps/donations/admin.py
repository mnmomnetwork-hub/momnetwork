from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("amount_cents", "donor_email", "status", "created_at", "stripe_session_id")
    list_filter = ("status", "created_at")
    search_fields = ("donor_email", "stripe_session_id")
