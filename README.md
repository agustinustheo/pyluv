# Website meant to share some of my APIs to the world

A web service containing an Indonesian SMS Classifier Model. Classifies SMS into 3 categories: Normal Message, Promotional Message, and Spam Message

A web service containing an English / Indonesian Fake News Identifier. Uses Google Search to help confirm the validity of an article by the articles' title.

Built using Django

## Branches

- **`master`**: modernised (Python 3.12, Django 6, uv, gunicorn).
- **[`original`](../../tree/original)**: the site as it was in 2019 (Django 2.1, commit `46ac465`).

## Run

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
uv run python manage.py test
```

| URL | What |
|---|---|
| `/`, `/home` | start page / home |
| `/blog/` | blog |
| `/api/` | API list |
| `/api/sms/id/classify?sms_text=<text>` | Indonesian SMS → `normal`, `promo` or `spam` |
| `/api/fakenews/en/classify?article=<url or title>` | similar articles found via Google (English) |
| `/api/fakenews/id/classify?article=<url or title>` | same, Indonesian |
| `/admin/` | Django admin |

Production: `gunicorn pyluv.wsgi` (see `Procfile`) with these environment variables:

| Variable | Default |
|---|---|
| `DJANGO_SECRET_KEY` | insecure development key, **set this** |
| `DJANGO_DEBUG` | `0` |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,[::1]` |
| `DATABASE_URL` | local SQLite file. For Postgres, `uv sync --extra postgres` and set it to a Postgres connection URL ([format](https://github.com/jazzband/dj-database-url#url-schema)) |

## What changed from `original`

- `requirements.txt` replaced by `pyproject.toml` + `uv.lock`. `Procfile` uses gunicorn.
- Django 2.1 → 6: `url()` → `re_path()`, `render_to_response` → `render`, `{% load staticfiles %}` → `{% load static %}`.
  Two migrations got the `pyluv_home` dependency they were missing, so a fresh database can be created.
- **Secrets removed from code.** The secret key and the Heroku Postgres credentials were hardcoded and are still in git
  history, so treat them as compromised. Settings now come from environment variables.
- SMS classifier: the 2019 pickles don't load with current scikit-learn. It now uses the paper's logistic-regression model
  from [sms-classifier-model](https://github.com/agustinustheo/sms-classifier-model) (master @ `b0f81ef`) with matching
  preprocessing. The model loads once per process. scikit-learn is pinned to the version that made the pickle.
- Fake news: the defunct `google` scraping package was replaced by `googlesearch-python`, and `newspaper3k` by `newspaper4k`.
  Two crashes were fixed: a `NameError` when a search result had an empty title, and a `numpy.matrix` input that current
  scikit-learn rejects.
- Removed committed `__pycache__` folders.

### Known limitation

Google now blocks search scraping without JavaScript, so the fake-news detectors currently get **no search results**.
The 2019 code had the same weakness. A real fix needs a search API (for example Brave Search or SerpAPI) and an API key.
