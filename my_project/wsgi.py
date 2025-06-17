"""
WSGI config for my_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

application = get_wsgi_application()

application = WhiteNoise(
        application,
        root=str(settings.STATIC_ROOT),  # Ensure path is a string
        prefix=settings.STATIC_URL,
        autorefresh=False
    )
    
    # Optionally serve media files if MEDIA_ROOT exists
if os.path.exists(settings.MEDIA_ROOT):
        application.add_files(str(settings.MEDIA_ROOT), prefix=settings.MEDIA_URL)

app = application  # For Vercel
