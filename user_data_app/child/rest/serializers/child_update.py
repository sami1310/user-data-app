from rest_framework import serializers
from child.models import Child
from user.rest.serializers.user import UserSerializer


class ChildUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Child
        fields = [
            "uid",
            "favorite_color",
            "user",
        ]

    def update(self, instance, validated_data):
        # Extracting user data
        user_data = validated_data.pop("user", {})
        user_instance = instance.user

        for attr, value in user_data.items():
            setattr(user_instance, attr, value)
        user_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
