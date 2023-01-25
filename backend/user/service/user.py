import bcrypt

from user.data.user import User
from user.repository.user import UserRepository
class UserService:
    user_repo = UserRepository()
    def create_user(self, password: str, email: str, name: str, ethereum_address: str) -> bool:
        hashed_password = bcrypt.hashpw(
            password=password.encode("utf-8"),
            salt=bcrypt.gensalt()
        ).decode("utf-8")

        if self.user_repo.create_user(email=email, name=name, password=hashed_password, ethereum_address=ethereum_address):
            return True
        return False

    def change_user(self, email: str, password: str, name: str, ethereum_address: str) -> User:
        hashed_password = bcrypt.hashpw(
            password=password.encode("utf-8"),
            salt=bcrypt.gensalt()
        ).decode("utf-8")

        result = self.user_repo.get_user_by_email(email=email)

        if result.password != hashed_password:
            result.password = hashed_password

        if result.name != name:
            result.name = result.name

        if result.ethereum_address != ethereum_address:
            result.ethereum_address = ethereum_address

        self.user_repo.save_user(user=result)

        return result

    def find_user(self, email: str | None, ethereum_address: str | None) -> User | None:
        if email and ethereum_address:
            return self.user_repo.get_user_by_email_and_address(email=email, ethereum_address=ethereum_address)

        if email and not ethereum_address:
            return self.user_repo.get_user_by_email(email=email)

        if not email and ethereum_address:
            return self.user_repo.get_user_by_address(ethereum_address=ethereum_address)

        return None

    def delete_user(self, ethereum_address: str, email: str) -> bool | None:
        result_email = self.user_repo.delete_user_by_email(email=email)
        result_address = self.user_repo.delete_user_by_address(ethereum_address=ethereum_address)

        if not result_address and not result_email:
            return None

        return True if result_address == True or result_email else False

    def login_user(self, ethereum_address: str, email: str, password: str) -> bool | None:
        result = None

        if email and ethereum_address:
            result = self.user_repo.get_user_by_email_and_address(email=email, ethereum_address=ethereum_address)

        if email and not ethereum_address:
            result = self.user_repo.get_user_by_email(email=email)

        if not email and ethereum_address:
            result = self.user_repo.get_user_by_address(ethereum_address=ethereum_address)

        if not result:
            return None

        return self.user_repo.check_password(email=email, ethereum_address=ethereum_address, password=password)