#!/bin/bash
apt-get update && apt-get install -y libpq-dev

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate