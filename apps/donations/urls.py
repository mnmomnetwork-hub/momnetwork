from django.urls import path
from .views import checkout, summary, stripe_webhook

urlpatterns = [
    path("checkout/", checkout, name="api-checkout"),
    path("donations/summary/", summary, name="api-donations-summary"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
]
