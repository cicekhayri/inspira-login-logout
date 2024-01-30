from src.model.user import User
from src.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user_by_email(self, email: str) -> User:
        return self._user_repository.get_user_by_email(email)

    def create_user(self, name: str, email: str, password: str) -> bool:
        new_user = User()
        new_user.name = name
        new_user.email = email
        new_user.set_password(password)

        return self._user_repository.create_user(new_user)
