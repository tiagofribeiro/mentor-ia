from rest_framework import serializers
from apps.chatbot.models import UploadedDocument

class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(write_only=True)
    response = serializers.CharField(read_only=True)

class UploadedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedDocument
        fields = ('file', 'title')