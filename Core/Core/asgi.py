"""
ASGI config for Core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from re import I

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from home.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')

application = get_asgi_application()

ws_patterns=[
    path("ws/test/",TestConsumer.as_asgi()),
    path('ws/new/',NewConsumer.as_asgi())
]
application=ProtocolTypeRouter(
    {
        'websocket' : URLRouter(ws_patterns)
    }
)
