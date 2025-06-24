from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.chatbot.serializers import ChatMessageSerializer
from apps.chatbot.services.chat_service import ChatService

class ChatMessageView(APIView):
    @extend_schema(
        request=ChatMessageSerializer,
        responses=ChatMessageSerializer,
        description="Envia uma mensagem para o bot."
    )
    def post(self, request: Request):
        try:
            serializer = ChatMessageSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            message = serializer.validated_data.get("message")
            response = ChatService.send(request.user, message)
            response_serializer = ChatMessageSerializer({"response": response})

            return Response(response_serializer.data, status.HTTP_200_OK)
        
        except Exception:
            return Response({"error": "Erro ao gerar resposta do bot."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)