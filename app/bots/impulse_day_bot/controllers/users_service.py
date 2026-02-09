from t_tech.invest import Client
from t_tech.invest.schemas import (
    GetInfoResponse,
    GetAccountsResponse,)


class UsersServiceBot:
    """
    Сервис для получения информации о пользователе и его счетах
    """

    def __init__(self, token, target):
        self.token = token
        self.target = target

    async def get_user_info(self) -> GetInfoResponse:
        """
        Получение информации о пользователе
        """
        with Client(self.token, target=self.target) as client:
            user_info = client.users.get_info()

        return user_info

    async def get_user_accounts(self) -> GetAccountsResponse:
        """
        Получение счетов пользователя
        """
        with Client(self.token, target=self.target) as client:
            accounts = client.users.get_accounts()

        return accounts