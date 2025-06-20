from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.chatbot.services.chat_service import ChatService

class ChatMessageView(APIView):
    """
    Envia uma mensagem ao modelo (com o histórico) e retorna a resposta.
    """
    def post(self, request):
        message = request.data.get("message")
        if not message:
            return Response({"error": "Mensagem não enviada."}, status=status.HTTP_400_BAD_REQUEST)
        resposta = ChatService.send(request.user, message)

        return Response({"response": resposta})