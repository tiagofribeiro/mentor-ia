from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.user.models import User
from apps.user.serializers import UserSerializer

class UserView(APIView):
    @extend_schema(
        responses=UserSerializer(many=True),
        description="Retorna todos os usuário padrão."
    )
    def get(self, request: Request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=UserSerializer,
        responses=UserSerializer,
        description="Cria um novo usuário."
    )
    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        