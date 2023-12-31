from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from parent.models import Parent
from user.rest.serializers.user import UserSerializer
from parent.rest.serilizers.parent_register import ParentSerializer


class UserParentDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        uid = self.kwargs.get("uid")

        try:
            user = User.objects.get(uid=uid)
            parent = Parent.objects.get(user=user)
        except User.DoesNotExist:
            raise ValueError("User with the specified UID does not exist")

        return user, parent

    def destroy(self, request, *args, **kwargs):
        instance, parent_instance = self.get_object()
        if instance and parent_instance:
            instance.delete()
            parent_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
