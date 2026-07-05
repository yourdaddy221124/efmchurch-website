# EFMC Church Website

A Django-powered website for the EFMC church.

## Development

```bash
# Setup virtual environment
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start dev server
python manage.py runserver
```

## Deployment

This project is deployed to Vercel. See the `vercel.json` configuration for details.
