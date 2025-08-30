from django.conf import settings
import stripe
from .models import Donation

def start_stripe_checkout(amount_cents: int) -> str:
    """Create a Stripe Checkout session. If Stripe isn't configured, redirect back gracefully."""
    if not settings.STRIPE_SECRET_KEY:
        # Graceful fallback when Stripe keys are missing
        return f"{settings.SITE_URL}/donate?status=unavailable"

    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "Donation to The Mom Network"},
                "unit_amount": int(max(200, amount_cents)),
            },
            "quantity": 1,
        }],
        success_url=f"{settings.SITE_URL}/donate?status=success",
        cancel_url=f"{settings.SITE_URL}/donate?status=cancelled",
    )
    Donation.objects.create(amount_cents=int(max(200, amount_cents)), stripe_session_id=session.id, status="created")
    return session.url
