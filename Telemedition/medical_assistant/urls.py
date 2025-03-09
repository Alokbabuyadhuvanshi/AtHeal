from django.urls import path
from .views import ChatView, MessageAPIView

urlpatterns = [
    path('', ChatView.as_view(), name='chat_home'), 
    path('api/message/', MessageAPIView.as_view(), name='api_message'), 
]
