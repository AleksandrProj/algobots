from t_tech.invest import Client
from t_tech.invest.schemas import (
    FindInstrumentResponse,
    InstrumentResponse,
    ShareResponse,
    SharesResponse,
    TradingSchedulesResponse)


class InstrumentsServiceBot:
    @staticmethod
    async def find_instrument(token, target, query, type_instrument) -> FindInstrumentResponse:
        """
        Поиск инструмента по query
        """
        with Client(token, target=target) as client:
            instruments = client.instruments.find_instrument(
                query=query,
                instrument_kind=type_instrument,
                api_trade_available_flag=True,)

        return instruments

    @staticmethod
    async def get_instrument_by(token, target, id_instrument) -> InstrumentResponse:
        """
        Получение основной информации об инструменте
        """
        with Client(token, target=target) as client:
            instrument = client.instruments.get_instrument_by(
                id=id_instrument,)

        return instrument

    @staticmethod
    async def get_shares(token, target) -> SharesResponse:
        """
        Получение списка акций
        """
        with Client(token, target=target) as client:
            shares = client.instruments.shares()

        return shares

    @staticmethod
    async def get_share_by(token, target, id_share) -> ShareResponse:
        """
        Получение акции по ее индентификатору
        """
        with Client(token, target=target) as client:
            share = client.instruments.share_by(id=id_share)

        return share

    @staticmethod
    async def get_trading_schedules(token, target, exchange) -> TradingSchedulesResponse:
        """
        Получение расписания торгов торговых площадок
        """
        with Client(token, target=target) as client:
            trading_schedules = client.instruments.trading_schedules(exchange=exchange)

        return trading_schedules