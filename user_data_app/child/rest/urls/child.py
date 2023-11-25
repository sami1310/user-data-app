from django.urls import path
from child.rest.views import child_register

urlpatterns = [
    path("", child_register.childList.as_view(), name="child-list"),
]
