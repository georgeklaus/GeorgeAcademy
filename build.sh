#!/bin/bash
set -ex

echo "🚀 NUCLEAR DEPLOYMENT INITIATED..."

# 1. Clean everything
rm -rf staticfiles node_modules
mkdir -p staticfiles

# 2. Install Python dependencies
pip install --upgrade --no-cache-dir pip
pip install --no-cache-dir -r requirements.txt

# 3. Install Node.js dependencies
npm install serve-handler

# 4. Collect static files
python manage.py collectstatic --noinput --clear --verbosity 3

# 5. Create verification
echo "STATIC_FILES_VERIFIED" > staticfiles/.verified
find staticfiles/ -type f > staticfiles/manifest.txt

# 6. Final check
echo "📁 DEPLOYMENT CONTENTS:"
find staticfiles/ -type f | head -50
du -sh staticfiles/

echo "✅ NUCLEAR DEPLOYMENT COMPLETE"