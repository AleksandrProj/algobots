from t_tech.invest import Client
from t_tech.invest.schemas import (
    FindInstrumentRequest,
    FindInstrumentResponse,\
    InstrumentRequest,
    InstrumentResponse,
    ShareResponse,
    SharesResponse,
    TradingSchedulesRequest,
    TradingSchedulesResponse,
    FutureResponse,
    FuturesResponse,
    GetFuturesMarginRequest,
    GetFuturesMarginResponse,)

class InstrumentsServiceBot:
    """
    Сервис информации о ценных бумагах
    """
    def __init__(self, token, target):
        self.token = token
        self.target = target

    async def find_instrument(self, data: FindInstrumentRequest) -> FindInstrumentResponse:
        """
        Поиск инструмента по query
        """
        with Client(self.token, target=self.target) as client:
            instruments = client.instruments.find_instrument(query=data.query)

        return instruments

    async def get_instrument_by(self, instrument: InstrumentRequest) -> InstrumentResponse:
        """
        Получение основной информации об инструменте
        """
        with Client(self.token, target=self.target) as client:
            instrument = client.instruments.get_instrument_by(id=instrument.id,)

        return instrument

    async def get_shares(self) -> SharesResponse:
        """
        Получение списка акций
        """
        with Client(self.token, target=self.target) as client:
            shares = client.instruments.shares()

        return shares

    async def get_share_by(self, share: InstrumentRequest) -> ShareResponse:
        """
        Получение акции по ее индентификатору
        """
        with Client(self.token, target=self.target) as client:
            share = client.instruments.share_by(id=share.id)

        return share

    async def get_futures(self) -> FuturesResponse:
        """
        Получение списка фьючерсов
        """
        with Client(self.token, target=self.target) as client:
            futures = client.instruments.futures()

        return futures

    async def get_future_by(self, future: InstrumentRequest) -> FutureResponse:
        """
        Получение фьючерса по его индентификатору
        """
        with Client(self.token, target=self.target) as client:
            future = client.instruments.future_by(id=future.id)

        return future

    async def get_futures_margin(self, future: GetFuturesMarginRequest) -> GetFuturesMarginResponse:
        """
        Получение гарантийного обеспечения по фьючерсам
        """
        with Client(self.token, target=self.target) as client:
            futures_margin = client.instruments.get_futures_margin(instrument_id=future.instrument_id)

        return futures_margin

    async def get_trading_schedules(self, schedule: TradingSchedulesRequest) -> TradingSchedulesResponse:
        """
        Получение расписания торгов торговых площадок
        """
        with Client(self.token, target=self.target) as client:
            trading_schedules = client.instruments.trading_schedules(exchange=schedule.exchange)

        return trading_schedules