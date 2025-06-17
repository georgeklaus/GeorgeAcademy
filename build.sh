#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files (always to $STATIC_ROOT, which should be BASE_DIR/staticfiles)

python manage.py collectstatic --noinput --clear --verbosity 0