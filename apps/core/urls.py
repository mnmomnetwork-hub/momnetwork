from django.urls import path
from .views import (
    home, donate_page, mission, who_we_help, videos, winners_page,
    resources, share_story_page, contact_page, privacy, terms, faq
)

urlpatterns = [
    path("", home, name="home"),
    path("donate", donate_page, name="donate"),
    path("mission", mission, name="mission"),
    path("who-we-help", who_we_help, name="who-we-help"),
    path("videos", videos, name="videos"),
    path("winners", winners_page, name="winners"),
    path("resources", resources, name="resources"),
    path("share-story", share_story_page, name="share-story"),
    path("contact", contact_page, name="contact"),
    path("privacy", privacy, name="privacy"),
    path("terms", terms, name="terms"),
    path("faq", faq, name="faq"),
]
