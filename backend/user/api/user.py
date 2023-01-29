from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.serializers.user import UserSerializer
from user.service.user import UserService



class UserLoginLogoutAPI(CreateAPIView, RetrieveAPIView):
    serializer_class = UserSerializer
    user_service = UserService()

    def post(self, requests, *args, **kwargs):
        user = self.user_service.find_user(
            email=requests.data.get("email"),
            ethereum_address=requests.data.get("ethereum_address"),
        )

        if not user:
            return Response(
                {"message": "This user not existed"}, status=status.HTTP_404_NOT_FOUND
            )

        if not self.user_service.login_user(
            email=requests.data.get("email"),
            ethereum_address=requests.data.get("ethereum_address"),
            password=requests.data.get("password")
        ):
            return Response(
                {"message": "Password or Something is going wrong"}, status=status.HTTP_404_NOT_FOUND
            )

        token = TokenObtainPairSerializer.get_token(user=user)
        refresh_token = str(token.refresh_token)
        access_token = str(token.access_token)
        response = Response(
            {
                "user": user.email,
                "message": "login success",
                "jwt_token": {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                },
            },
            status=status.HTTP_201_CREATED
        )

        return response

class UserCreateRetrieveAPI(CreateAPIView, RetrieveAPIView):
    serializer_class = UserSerializer
    user_service = UserService()

    def post(self, requests, *args, **kwargs):

        res = self.user_service.create_user(
            email=requests.data.get("email"),
            password=requests.data.get("password"),
            name=requests.data.get("name"),
            ethereum_address=requests.data.get("ethereum_address")
        )

        if not res:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, requests, *args, **kwargs):
        res = self.user_service.find_user(email=requests.data.get("email"), ethereum_address=requests.data.get("ethereum_address"))

        if not res:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK, content=res)