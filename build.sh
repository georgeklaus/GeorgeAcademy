#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Vercel-specific setup
if [ "$VERCEL" == "1" ]; then
    # Create directories (if needed)
    mkdir -p /var/task/staticfiles
    mkdir -p /var/task/media

    # Collect static files to Vercel location
    python manage.py collectstatic --noinput --clear --verbosity 0

    # Verify collection
    echo "Static files collected:"
    find /var/task/staticfiles -type f | wc -l
else
    # Local development
    python manage.py collectstatic --noinput
fi