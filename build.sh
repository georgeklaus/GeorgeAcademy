#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "Installing dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Python version:"
python --version

echo "Running collectstatic..."
python manage.py collectstatic --noinput --clear

echo "Contents of staticfiles directory:"
ls -l staticfiles