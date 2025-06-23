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

echo "➤ Verifying file structure..."
find staticfiles/ -type f | head -20
du -sh staticfiles/

ls -l staticfiles/

echo "----- Build Completed -----"
# Ensure the script exits with a success status
exit 0
echo "Build script executed successfully."
echo "Exiting with status code $?"
echo "----- Build Script Finished -----"
echo "Build script executed successfully."
echo "Exiting with status code $?"
