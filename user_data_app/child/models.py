from django.db import models
from django.db import models
from core.models import CustomeBase
from parent.models import Parent
from django.conf import settings


class Child(CustomeBase):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="child",
        null=True,
        blank=True,
    )
    parents = models.ManyToManyField(Parent, related_name="children")
    favorite_color = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Child)"
