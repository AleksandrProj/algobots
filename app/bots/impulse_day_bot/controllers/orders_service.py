from t_tech.invest import Client
from t_tech.invest.schemas import (
    PostOrderResponse,
    PostOrderAsyncResponse,
    CancelOrderResponse,
    OrderState,
    GetOrdersResponse,)


class OrdersServiceBot:
    """
    Сервис работы с торговыми поручениями
    """
    def __init__(self, token, target):
        self.token = token
        self.target = target

    async def post_order_async(self, query, type_instrument) -> PostOrderAsyncResponse:
        """
        Асинхронное выставление заявки
        """
        pass

    async def post_order(self, query, type_instrument) -> PostOrderResponse:
        """
        Выставление заявки
        """
        pass

    async def cancel_order(self, query, type_instrument) -> CancelOrderResponse:
        """
        Отмена выставленной заявки
        """
        pass

    async def get_order_state(self, query, type_instrument) -> OrderState:
        """
        Получение статуса торгового поручения
        """
        pass

    async def get_orders(self, query, type_instrument) -> GetOrdersResponse:
        """
        Получение списка активных заявок по счету
        """
        pass