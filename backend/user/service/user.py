import bcrypt

from user.repository.user import UserRepository
class UserService:
    user_repo = UserRepository()
    def create_user(self, password: str, email: str, name: str) -> bool:
        hashed_password = bcrypt.hashpw(
            password=password.encode("utf-8"),
            salt=bcrypt.gensalt()
        ).decode("utf-8")

        if self.user_repo.create_user(email=email, name=name, password=hashed_password):
            return True
        return False
