from t_tech.invest import Client
from t_tech.invest.schemas import (
    GetInfoResponse, GetAccountsResponse)


class UsersServiceBot:
    @staticmethod
    async def get_user_info(token, target) -> GetInfoResponse:
        """
        Получение информации о пользователе
        """
        with Client(token, target=target) as client:
            user_info = client.users.get_info()

        return user_info

    @staticmethod
    async def get_user_accounts(token, target) -> GetAccountsResponse:
        """
        Получение счетов пользователя
        """
        with Client(token, target=target) as client:
            accounts = client.users.get_accounts()

        return accounts