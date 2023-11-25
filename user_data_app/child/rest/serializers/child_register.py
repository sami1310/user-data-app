from rest_framework import serializers
from child.models import Child
from user.models import User
from user.rest.serializers.user import UserSerializer
from parent.rest.serilizers.parent_register import ParentSerializer


class ChildSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    parents = ParentSerializer(many=True)

    class Meta:
        model = Child
        fields = ["uid", "parents", "favorite_color", "user"]
