from rest_framework import serializers
from parent.models import Parent
from user.rest.serializers.user import UserSerializer

# class ParentUpdateSerializer(serializers.Serializer):
#     street = serializers.CharField(max_length=255, required=False)
#     city = serializers.CharField(max_length=100, required=False)
#     state = serializers.CharField(max_length=100, required=False)
#     zip_code = serializers.CharField(max_length=10, required=False)

#     def update(self, instance, validated_data):
#         # Update fields based on validated_data
#         instance.street = validated_data.get("street", instance.street)
#         instance.city = validated_data.get("city", instance.city)
#         instance.state = validated_data.get("state", instance.state)
#         instance.zip_code = validated_data.get("zip_code", instance.zip_code)

#         return instance


class ParentUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Parent
        fields = ["uid", "street", "city", "state", "zip_code", "user"]

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
