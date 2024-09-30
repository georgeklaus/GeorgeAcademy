"""
WSGI config for my_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()  # Load the environment variables from your .env file

# Set the default settings module for the 'wsgi' command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
