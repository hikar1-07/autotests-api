from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class PublicUsersRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str



class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    PublicUsersClient – для публичных методов, не требующих авторизации.

    """

    def create_user_api(self, request: PublicUsersRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь (email, password, lastName, firstName, middleName)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)