from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from apps.winners.models import WeeklyWinner
from apps.stories.forms import StoryForm
from apps.contact.forms import ContactForm
from apps.donations.utils import start_stripe_checkout

def home(request):
    return render(request, "home.html")

@require_http_methods(["GET", "POST"])
def donate_page(request):
    amount = int(request.GET.get("amount") or request.POST.get("amount") or 2)
    if request.method == "POST":
        session_url = start_stripe_checkout(amount_cents=max(200, int(amount) * 100))
        return redirect(session_url)
    return render(request, "donate.html", {"amount": amount})

def mission(request):
    return render(request, "mission.html")

def who_we_help(request):
    return render(request, "who_we_help.html")

def videos(request):
    return render(request, "videos.html")

def winners_page(request):
    winners = WeeklyWinner.objects.order_by("-date")[:52]
    return render(request, "winners.html", {"winners": winners})

def resources(request):
    return render(request, "resources.html")

@require_http_methods(["GET", "POST"])
def share_story_page(request):
    submitted = False
    form = StoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.status = "pending"
        obj.save()
        submitted = True
        form = StoryForm()
    return render(request, "share_story.html", {"form": form, "submitted": submitted})

@require_http_methods(["GET", "POST"])
def contact_page(request):
    sent = False
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save_and_notify()
        sent = True
        form = ContactForm()
    return render(request, "contact.html", {"form": form, "sent": sent})

def privacy(request):
    return render(request, "privacy.html")

def terms(request):
    return render(request, "terms.html")

def faq(request):
    return render(request, "faq.html")
