from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from core.models import CustomeBase
from .managers import CustomUserManager
from .choices import GENDER_CHOICE, ROLE_CHOICE

# Create your models here.


class User(CustomeBase, AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICE, null=True, blank=True
    )
    user_role = models.CharField(
        max_length=25, choices=ROLE_CHOICE, null=True, blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @staticmethod
    def has_module_perms(app_label):
        return True

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    def __str__(self):
        return self.email
