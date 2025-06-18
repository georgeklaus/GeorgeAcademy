#!/bin/bash
# build.sh
echo "Installing dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --noinput --clear

echo "Contents of staticfiles directory:"
ls -l staticfiles