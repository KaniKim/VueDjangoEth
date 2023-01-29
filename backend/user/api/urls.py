from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from user.api.user import UserCreateRetrieveAPI,UserLoginLogoutAPI
urlpatterns = [
    path("login/", UserLoginLogoutAPI.as_view(), name="user_login"),
    path("", UserCreateRetrieveAPI.as_view(), name="user"),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]