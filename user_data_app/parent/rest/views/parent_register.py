from rest_framework import generics
from parent.models import Parent
from parent.rest.serilizers.parent_register import (
    ParentRegisterSerializer,
    ParentSerializer,
)


class ParentRegister(generics.CreateAPIView):
    serializer_class = ParentRegisterSerializer


class ParentList(generics.ListAPIView):
    # permission_classes = [AllowAny]
    serializer_class = ParentSerializer
    queryset = Parent.objects.filter()
