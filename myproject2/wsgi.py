"""
WSGI config for myproject2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject2.settings')

# Vercel が認識できるように、変数名を 'application' から 'handler' に変更
handler = get_wsgi_application()