"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

# touched on 2025-07-09T21:53:59.828998Z
# touched on 2025-07-09T21:54:18.512586Z
# touched on 2025-07-09T21:55:24.275346Z
# touched on 2025-07-09T21:55:29.630886Z