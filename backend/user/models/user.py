from django.db import models
from django.db.models import CharField, EmailField, BooleanField, UUIDField, DateTimeField
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    id = UUIDField(primary_key=True, max_length=64, unique=True, null=False)
    name = CharField(max_length=255, unique=False)
    email = EmailField(unique=True)
    password = CharField(max_length=255, null=False, blank=False)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True, blank=True)
    updated_at = DateTimeField(auto_now_add=True, blank=True)
    login_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    ethereum_address = CharField(max_length=255, null=True)

    class Meta:
        app_label = "user"