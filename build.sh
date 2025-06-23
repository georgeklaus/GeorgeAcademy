#!/bin/bash
set -e

echo "----- Build Started -----"

# Create necessary directories
rm -rf staticfiles/ || true
mkdir -p staticfiles
mkdir -p media

echo "--- Installing dependencies ---"
pip install --upgrade pip
pip install whitenoise==6.9.0  # Explicit install for consistency
pip install -r requirements.txt

echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

echo "--- Verifying static files ---"
ls -l staticfiles/

echo "----- Build Completed -----"