#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create Vercel-specific static directory
mkdir -p /var/task/staticfiles

# Collect static files
python manage.py collectstatic --noinput --verbosity 0

# Verify files were collected
echo "Collected static files:"
find /var/task/staticfiles -type f | wc -l

# Verify template exists
echo "Checking for template:"
find . -name login_registration.html


{
  "scripts": {
    "vercel-build": "chmod +x build.sh && ./build.sh"
  }
}