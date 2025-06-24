from rest_framework import serializers
from apps.chatbot.models import ChatMessage, ChatSession, UploadedDocument

class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(write_only=True)
    response = serializers.CharField(read_only=True)