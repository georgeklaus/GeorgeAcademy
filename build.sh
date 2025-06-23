#!/bin/bash
set -e

echo "----- Build Started -----"

# Create necessary directories
mkdir -p staticfiles
mkdir -p media

echo "--- Installing dependencies ---"
pip install --upgrade pip
pip install -r requirements.txt

echo "--- Collecting static files ---"
python manage.py collectstatic --noinput --clear

echo "--- Verifying static files ---"
ls -l staticfiles/

echo "----- Build Completed -----"