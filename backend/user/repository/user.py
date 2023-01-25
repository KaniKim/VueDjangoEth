import datetime
import uuid

from django.db.models import Q

from user.models.user import User as UserModel
from user.data.user import User as UserData

class UserRepository:
    @classmethod
    def to_django_model(cls, user_data: UserData) -> UserModel:
        return UserModel(
            id=user_data.id,
            name=user_data.name,
            email=user_data.email,
            is_active=user_data.is_active,
            is_staff=user_data.is_staff,
            is_superuser=user_data.is_superuser,
            created_at=user_data.created_at,
            updated_at=user_data.updated_at,
            login_at=user_data.login_at,
            ethereum_address=user_data.ethereum_address
        )

    @classmethod
    def to_data(cls, user_model: UserModel) -> UserData:
        return UserData(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            is_staff=user_model.is_staff,
            is_active=user_model.is_active,
            is_superuser=user_model.is_superuser,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
            login_at=user_model.login_at,
            ethereum_address=user_model.ethereum_address
        )

    def get_user_by_address(self, ethereum_address: str) -> UserData | None:
        result = UserModel.objects.filter(ethereum_address=ethereum_address).first()

        if not result:
            return None
        return self.to_data(result)

    def get_user_by_email_and_address(self, email: str, ethereum_address: str) -> UserData | None:
        result = UserModel.objects.filter(Q(email=email) and Q(ethereum_address=ethereum_address)).first()

        if not result:
            return None

        return self.to_data(user_model=result)

    def get_user_by_email(self, email: str) -> UserData | None:
        result = UserModel.objects.filter(email=email).first()

        if not result:
            return None
        return self.to_data(result)

    # noinspection PyMethodMayBeStatic
    def change_user_address(self, email: str, new_ethereum_address: str) -> bool | None:
        result = UserModel.objects.filter(email=email).first()

        if not result:
            return None

        if result.ethereum_address == new_ethereum_address:
            return False

        result.ethereum_address = new_ethereum_address
        result.save()
        return True


    # noinspection PyMethodMayBeStatic
    def delete_user_by_address(self, ethereum_address: str) -> bool | None:
        result = UserModel.objects.filter(ethereum_address=ethereum_address).first()

        if not result:
            return None

        if result.is_active:
            result.is_active = False
            result.save()
        else:
            return False
        return True

    # noinspection PyMethodMayBeStatic
    def delete_user_by_email(self, email: str) -> bool | None:
        result = UserModel.objects.filter(email=email).first()

        if not result:
            return None

        if result.is_active:
            result.is_active = False
            result.save()
        else:
            return False
        return True

    def create_user(self, email: str, ethereum_address: str, password: str, name: str) -> bool:
        user_data = UserData(
            id=str(uuid.uuid4()),
            email=email,
            password=password,
            name=name,
            is_active=False,
            is_superuser=False,
            is_staff=False,
            ethereum_address=ethereum_address,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            login_at=None,
        )
        user_model = self.to_django_model(user_data=user_data)
        if user_model.save():
            return True
        return False


    def save_user(self, user: UserData) -> bool:

        try:
            user_model = self.to_django_model(user_data=user)
            user_model.save()

        except Exception as e:
            raise e

        finally:
            return True

