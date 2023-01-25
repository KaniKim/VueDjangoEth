
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from user.serializers.user import UserSerializer
from user.service.user import UserService


class UserCreateRetrieveAPI(CreateAPIView, RetrieveAPIView):
    serializer_class = UserSerializer
    user_service = UserService()

    def post(self, requests, *args, **kwargs):
        res = self.user_service.create_user(
            email=self.kwargs.get("email"),
            password=self.kwargs.get("password"),
            name=self.kwargs.get("name"),
            ethereum_address=self.kwargs.get("ethereum_address")
        )

        if not res:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, requests, *args, **kwargs):
        res = self.user_service.find_user(email=self.kwargs.get("email"), ethereum_address=self.kwargs.get("ethereum_address"))

        if not res:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK, content=res)