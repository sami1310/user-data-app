from rest_framework import generics
from child.models import Child
from child.rest.serializers.child_register import ChildSerializer


class childList(generics.ListAPIView):
    serializer_class = ChildSerializer
    queryset = Child.objects.filter()
