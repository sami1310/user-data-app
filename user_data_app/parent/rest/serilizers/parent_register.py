from rest_framework import serializers
from parent.models import Parent
from user.models import User
from user.rest.serializers.user import UserSerializer


class ParentRegisterSerializer(serializers.Serializer):
    user = UserSerializer()
    password = serializers.CharField(write_only=True)
    street = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    zip_code = serializers.CharField(max_length=10)

    def create(self, validated_data):
        user_data = validated_data.get("user")
        password = validated_data.get("password")
        street = validated_data.get("street")
        city = validated_data.get("city")
        state = validated_data.get("state")
        zip_code = validated_data.get("zip_code")

        user = User.objects.create(
            email=user_data.get("email"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            gender=user_data.get("gender"),
            user_role="Parent",
        )

        user.set_password(password)
        user.save()

        parent = Parent.objects.create(
            user=user,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            is_parent=True,
        )

        return parent
