import datetime

from django.db import models
from django.db.models import CharField, EmailField, BooleanField, UUIDField, DateTimeField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    id = UUIDField(max_length=64, unique=True, null=False)
    name = CharField(max_length=255, unique=False)
    email = EmailField(unique=True)
    password = CharField(null=False, blank=False)
    is_active = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        app_label = "user"