from rest_framework.serializers import Serializer, UUIDField, CharField, EmailField, BooleanField, DateTimeField

class UserSerializer(Serializer): # noqa
    id = UUIDField(read_only=True)
    name = CharField(required=True, max_length=255)
    email = EmailField(required=True)
    password = CharField(write_only=True)
    ethereum_address = CharField(required=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
    login_at = DateTimeField(read_only=True)

