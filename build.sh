#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Upgrade pip to the latest version
pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run database migrations
python manage.py migrate --noinput

# Collect static files into $STATIC_ROOT (usually BASE_DIR/staticfiles)
python manage.py collectstatic --noinput --clear --verbosity 0