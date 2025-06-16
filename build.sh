#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate
{
  "scripts": {
    "vercel-build": "chmod +x build.sh && ./build.sh"
  }
}