from rest_framework import serializers
from apps.user.models import User

class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', 'is_active')
        read_only_fields = ('id', 'is_active', 'is_staff')

    def create_user_instance(self, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        return self.create_user_instance(validated_data)

class UserSerializer(BaseUserSerializer):
    def create_user_instance(self, validated_data):
        return User.objects.create_user(**validated_data)

class SuperUserSerializer(BaseUserSerializer):
    def create_user_instance(self, validated_data):
        return User.objects.create_superuser(**validated_data)