from rest_framework import serializers
from child.models import Child
from parent.models import Parent
from user.models import User
from user.rest.serializers.user import UserSerializer
from parent.rest.serilizers.parent_register import ParentSerializer


class ChildSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    parents = ParentSerializer(many=True)

    class Meta:
        model = Child
        fields = ["uid", "parents", "favorite_color", "user"]


class ChildRegisterSerializer(serializers.Serializer):
    user = UserSerializer()
    password = serializers.CharField(write_only=True)
    parent_uids = serializers.ListField(
        child=serializers.UUIDField(), required=False
    )  # getting parents uid for assiging
    favorite_color = serializers.CharField(max_length=255)

    def create(self, validated_data):
        user_data = validated_data.get("user")
        password = validated_data.get("password")
        parent_uids = validated_data.get("parent_uids", [])
        favorite_color = validated_data.get("favorite_color")

        user = User.objects.create(
            email=user_data.get("email"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            gender=user_data.get("gender"),
            user_role="Child",
        )

        user.set_password(password)
        user.save()

        child = Child.objects.create(
            user=user,
            favorite_color=favorite_color,
        )

        for parent_uid in parent_uids:
            try:
                parent = Parent.objects.get(uid=parent_uid)
                child.parents.add(parent)
            except Parent.DoesNotExist:
                raise serializers.ValidationError(
                    f"Parent with UID {parent_uid} does not exist."
                )

        return child
