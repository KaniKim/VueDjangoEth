from user.serializers.user import UserSerializer
from user.service.user import UserService

from rest_framework.generics import GenericAPIView, CreateAPIView

class UserCreateAPI(GenericAPIView, CreateAPIView):
    serializer_class = UserSerializer
    user_service = UserService()

    def post(self, request):
        return self.user_service.create_user(
            email=request.get("email"),
            password=request.get("password"),
            name=request.get("name")
        )