from django.urls import path
from apps.chatbot.api.chat import ChatMessageView

urlpatterns = [
    path('message/', ChatMessageView.as_view(), name='chatbot-message'),
]