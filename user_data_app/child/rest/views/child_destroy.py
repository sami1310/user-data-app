from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from child.models import Child
from user.rest.serializers.user import UserSerializer


class UserChildDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        uid = self.kwargs.get("uid")

        try:
            user = User.objects.get(uid=uid)  # getting user
            child = Child.objects.get(
                user=user
            )  # Getting child instance associated with the user
        except User.DoesNotExist:
            raise ValueError("User with the specified UID does not exist")

        return user, child

    # Deletion operation of child and associated user
    def destroy(self, request, *args, **kwargs):
        instance, child_instance = self.get_object()
        if instance and child_instance:
            instance.delete()
            child_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
