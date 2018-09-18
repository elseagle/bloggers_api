"""
WSGI config for bloggers_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
application = DjangoWhiteNoise(application)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bloggers_project.settings")
application = get_wsgi_application()

