import os
import logging
from configparser import ConfigParser

from aiohttp import ClientSession
from dotenv import load_dotenv

from t_tech.invest.constants import INVEST_GRPC_API, INVEST_GRPC_API_SANDBOX

from app.bots.impulse_day_bot.utils.common import is_sandbox

from .users_service import UsersServiceBot
from .instruments_service import InstrumentsServiceBot

load_dotenv()
config_obj = ConfigParser()
config_obj.read("config.ini")

logger = logging.getLogger(__name__)

class Bot:
    target = INVEST_GRPC_API_SANDBOX if is_sandbox else INVEST_GRPC_API
    token = os.getenv("TBANK_SANDBOX_TOKEN") if is_sandbox else os.getenv("TBANK_TOKEN")
    url = os.getenv("TBANK_URL_SANDBOX") if is_sandbox else os.getenv("TBANK_URL_PROD")

    def __init__(self, session_bot: ClientSession):
        self.session_bot = session_bot
        self.account = config_obj['ACCOUNT']
        self.management = config_obj['MONEY-MANAGEMENT']
        self.strategy = config_obj['STRATEGY']

    def __repr__(self):
        return f"Бот для поиска первых импульсов дня"

    async def start_bot(self):
        """Запуск бота"""
        logging.info("Start bot...")


    @staticmethod
    async def end_bot():
        """Остановка бота"""
        logging.info("End bot...")