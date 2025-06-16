#!/bin/bash
apt-get update && apt-get install -y libpq-dev

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Run database migrations
python3 manage.py migrate