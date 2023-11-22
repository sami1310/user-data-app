from django.db import models
from django.db import models
from core.models import CustomeBase
from django.conf import settings
from .choices import PARENT_CHOICE


class Parent(CustomeBase):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="parent"
    )
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    is_parent = models.BooleanField(default=False, null=True, blank=True)
    parent_type = models.CharField(
        max_length=25, choices=PARENT_CHOICE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Parent)"
