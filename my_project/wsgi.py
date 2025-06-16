"""
WSGI config for my_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

application = get_wsgi_application()

# Use 'staticfiles' if that's your STATIC_ROOT, or 'static' if that's where your files are
static_root = os.path.join(os.path.dirname(__file__), 'staticfiles')
if not os.path.exists(static_root):
    static_root = os.path.join(os.path.dirname(__file__), 'static')

application = WhiteNoise(application, root=static_root)

# For Vercel compatibility
app = application  # Vercel looks for 'app' or 'handler'
