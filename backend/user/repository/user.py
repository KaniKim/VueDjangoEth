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
            is_superuser=user_data.is_superuser,
            created_at=user_data.created_at,
            updated_at=user_data.updated_at,
        )

    @classmethod
    def to_data(cls, user_model: UserModel) -> UserData:
        return UserData(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            is_active=user_model.is_active,
            is_superuser=user_model.is_superuser,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
        )

    def get_user_by_email(self, email: str) -> UserData | None:
        result = UserModel.objects.filter(email=email).first()

        if not result:
            return None
        return self.to_data(result)

    def create_user(self, user_data: UserData) -> bool:
        user_model = self.to_django_model(user_data=user_data)
        if user_model.save():
            return True
        return False


