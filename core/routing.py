from django.urls import path
from .consumers import CodeEditorConsumer

websocket_urlpatterns = [
    path('ws/editor/<str:room_name>/', CodeEditorConsumer.as_asgi()),
]
