import os
import logging

from aiohttp import ClientSession
from dotenv import load_dotenv
from t_tech.invest import FindInstrumentRequest

from t_tech.invest.constants import INVEST_GRPC_API, INVEST_GRPC_API_SANDBOX

from app.bots.impulse_day_bot.utils.common import is_sandbox

from .users_service import UsersServiceBot
from .instruments_service import InstrumentsServiceBot


load_dotenv()
logger = logging.getLogger(__name__)

class Bot:
    target = INVEST_GRPC_API_SANDBOX if is_sandbox else INVEST_GRPC_API
    token = os.getenv("TBANK_SANDBOX_TOKEN") if is_sandbox else os.getenv("TBANK_TOKEN")
    url = os.getenv("TBANK_URL_SANDBOX") if is_sandbox else os.getenv("TBANK_URL_PROD")

    def __init__(self, session_bot: ClientSession):
        self.session_bot = session_bot

    def __repr__(self):
        return f"Бот для поиска первых импульсов дня"

    async def start_bot(self):
        """Запуск бота"""
        logging.info("Start bot...")

        share = FindInstrumentRequest(query='moex')

        # instrument = InstrumentsServiceBot(self.token, self.target)
        # instrument_info = await instrument.find_instrument(share)
        # logger.info(instrument_info)


        # user = UsersServiceBot(self.token, self.target)
        # user_info = await user.get_user_info()
        # logger.info(user_info)

    @staticmethod
    async def end_bot():
        """Остановка бота"""
        logging.info("End bot...")