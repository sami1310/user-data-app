from rest_framework import generics
from parent.rest.serilizers.parent_register import ParentRegisterSerializer


class ParentRegister(generics.CreateAPIView):
    serializer_class = ParentRegisterSerializer
