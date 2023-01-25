from django.urls import path, include

from user.api.user import UserCreateRetrieveAPI
urlpatterns = [
    path("", UserCreateRetrieveAPI.as_view(), name="user")
]