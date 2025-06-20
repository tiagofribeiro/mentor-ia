from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from ..serializers import SuperUserSerializer

class SuperUserView(APIView):
    """
    Cria um novo super-usuário
    """
    @extend_schema(
        request=SuperUserSerializer,
        responses=SuperUserSerializer,
        description="Cria um novo usuário."
    )
    def post(self, request):
        serializer = SuperUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)