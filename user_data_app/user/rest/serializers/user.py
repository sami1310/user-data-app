from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["uid", "first_name", "last_name", "email", "gender", "user_role"]

    # Set email field as read-only
    email = serializers.EmailField(read_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["uid", "first_name", "last_name", "email", "gender", "user_role"]
