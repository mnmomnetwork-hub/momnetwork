# The Mom Network — Django (Full Templates + Admin + APIs)

Complete Django 5 stack with templates, admin, REST APIs, Stripe Checkout, and email.

## Quickstart

1) Python setup
- Python 3.12+
- python -m venv .venv && source .venv/bin/activate
- pip install -r requirements.txt

2) Env
- cp .env.example .env
- Set DJANGO_SECRET_KEY, SITE_URL, and (optional) STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET
- For Postgres in prod, set DATABASE_URL

3) DB and Admin
- python manage.py migrate
- python manage.py createsuperuser

4) Run
- python manage.py runserver
- Open http://localhost:8000

## Stripe (optional for live payments)
- Install Stripe CLI
- stripe listen --forward-to localhost:8000/api/stripe/webhook/
- Set STRIPE_WEBHOOK_SECRET from the CLI output in .env

## Routes

HTML:
- /
- /donate
- /mission, /who-we-help, /videos, /winners, /resources
- /share-story, /contact
- /privacy, /terms, /faq
- /admin/

APIs (DRF):
- POST/GET /api/entries/
- POST/GET /api/stories/ (GET returns approved + public)
- POST/GET /api/nominations/
- POST /api/checkout/        { "amount_cents": 500 }
- GET  /api/donations/summary/
- POST/GET /api/contact/
- GET/POST /api/winners/
- POST /api/stripe/webhook/   (Stripe)

## Management Commands
- python manage.py select_weekly_winner
- python manage.py reset_weekly_entries

## Static Files
- WhiteNoise serves static files in production
- Run python manage.py collectstatic during deployment

## Docker
- docker compose up --build

## Notes
- If Stripe keys are missing, checkout returns a friendly fallback URL so the page keeps working.
- Email defaults to console backend locally. Switch to SMTP by editing .env.
