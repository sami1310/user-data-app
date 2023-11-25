from rest_framework.generics import RetrieveUpdateAPIView
from child.models import Child
from child.rest.serializers.child_update import ChildUpdateSerializer


class UpdateChildInfo(RetrieveUpdateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildUpdateSerializer
    lookup_field = "uid"
