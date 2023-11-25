from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from parent.models import Parent
from parent.rest.serilizers.parent_update import ParentUpdateSerializer


class UpdateParentInfo(RetrieveUpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentUpdateSerializer
    lookup_field = "uid"
    # permission_classes = [IsAuthenticated]

    # def get_object(self):
    #     # Returns the Parent instance associated with the user
    #     return self.request.user.parent

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)
