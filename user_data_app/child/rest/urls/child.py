from django.urls import path
from child.rest.views import child_register, child_update, child_destroy

urlpatterns = [
    path(
        "/delete/<uuid:uid>",
        child_destroy.UserChildDeleteView.as_view(),
        name="destroy-parent",
    ),
    path(
        "/<uuid:uid>", child_update.UpdateChildInfo.as_view(), name="update-child-info"
    ),
    path("/register", child_register.ChildRegister.as_view(), name="child-register"),
    path("", child_register.childList.as_view(), name="child-list"),
]
