import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cce.settings') 

######### custom settings ############
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from app.routing import websocket_urlpatterns
  
application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    "websocket" : OriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),["*"]),
})

