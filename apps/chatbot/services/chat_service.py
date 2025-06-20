from apps.chatbot.langchain.client import send_prompt
from apps.chatbot.models import ChatSession, ChatMessage

class ChatService:
    @staticmethod
    def get_or_create_session(user):
        session, _ = ChatSession.objects.get_or_create(user=user)

        return session

    @staticmethod
    def get_history(session):
        messages = ChatMessage.objects.filter(session=session).order_by("timestamp")
        history = []
        for msg in messages:
            role = "user" if msg.sender == "user" else "assistant"
            history.append({"role": role, "content": msg.content})
            
        return history
    
    @staticmethod
    def send(user, message, system_prompt=None):
        session = ChatService.get_or_create_session(user)
        ChatMessage.objects.create(session=session, sender="user", content=message)
        history = ChatService.get_history(session)
        if system_prompt:
            history.insert(0, {"role": "system", "content": system_prompt})
        response = send_prompt(message, system_prompt=system_prompt, history=history)
        ChatMessage.objects.create(session=session, sender="bot", content=response)

        return response