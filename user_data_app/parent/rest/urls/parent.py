from django.urls import path
from parent.rest.views import parent_register, parent_update, parent_destroy

urlpatterns = [
    path(
        "/delete/<uuid:uid>",
        parent_destroy.UserParentDeleteView.as_view(),
        name="destroy-parent",
    ),
    path(
        "/register",
        parent_register.ParentRegister.as_view(),
        name="parent-register",
    ),
    path(
        "/<uuid:uid>",
        parent_update.UpdateParentInfo.as_view(),
        name="update-parent-info",
    ),
    # path(
    #     "/update",
    #     parent_update.UpdateParentInfo.as_view(),
    #     name="update-parent-info",
    # ),
    path("", parent_register.ParentList.as_view(), name="parent-list"),
]
