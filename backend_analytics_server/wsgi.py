"""
WSGI config for backend_analytics_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')

application = get_wsgi_application()

# Usar settings.STATIC_ROOT para asegurar la ruta correcta
if not settings.DEBUG:
    application = WhiteNoise(application, root=settings.STATIC_ROOT)