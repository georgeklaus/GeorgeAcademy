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
if not settings.DEBUG:
    application = WhiteNoise(
        application,
        root=settings.STATIC_ROOT,
        prefix=settings.STATIC_URL
    )
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'staticfiles'))

app = application  # For Vercel
