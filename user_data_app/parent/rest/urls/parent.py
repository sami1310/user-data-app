from django.urls import path
from parent.rest.views import parent_register

urlpatterns = [
    path(
        "/register",
        parent_register.ParentRegister.as_view(),
        name="parent-register",
    ),
]
