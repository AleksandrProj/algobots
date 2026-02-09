from t_tech.invest import Client
from t_tech.invest.schemas import (
    FindInstrumentResponse,
    InstrumentResponse,
    ShareResponse,
    SharesResponse,
    TradingSchedulesResponse)


class InstrumentsServiceBot:
    """
    Сервис информации о ценных бумагах
    """

    def __init__(self, token, target):
        self.token = token
        self.target = target

    async def find_instrument(self, query, type_instrument) -> FindInstrumentResponse:
        """
        Поиск инструмента по query
        """
        with Client(self.token, target=self.target) as client:
            instruments = client.instruments.find_instrument(
                query=query,
                instrument_kind=type_instrument,
                api_trade_available_flag=True,)

        return instruments

    async def get_instrument_by(self, id_instrument) -> InstrumentResponse:
        """
        Получение основной информации об инструменте
        """
        with Client(self.token, target=self.target) as client:
            instrument = client.instruments.get_instrument_by(
                id=id_instrument,)

        return instrument

    async def get_shares(self) -> SharesResponse:
        """
        Получение списка акций
        """
        with Client(self.token, target=self.target) as client:
            shares = client.instruments.shares()

        return shares

    async def get_share_by(self, id_share) -> ShareResponse:
        """
        Получение акции по ее индентификатору
        """
        with Client(self.token, target=self.target) as client:
            share = client.instruments.share_by(id=id_share)

        return share

    async def get_trading_schedules(self, exchange) -> TradingSchedulesResponse:
        """
        Получение расписания торгов торговых площадок
        """
        with Client(self.token, target=self.target) as client:
            trading_schedules = client.instruments.trading_schedules(exchange=exchange)

        return trading_schedules