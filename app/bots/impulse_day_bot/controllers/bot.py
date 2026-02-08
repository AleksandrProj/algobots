import os
import logging

from aiohttp import ClientSession
from dotenv import load_dotenv

from t_tech.invest.constants import INVEST_GRPC_API

from app.bots.impulse_day_bot.controllers import (
    UsersServiceBot,
    InstrumentsServiceBot,)


load_dotenv()
logger = logging.getLogger(__name__)


class Bot(UsersServiceBot, InstrumentsServiceBot):
    target = INVEST_GRPC_API

    def __init__(self, session_bot: ClientSession):
        self.session_bot = session_bot
        self.token = os.getenv("TBANK_TOKEN")
        self.sandbox_token = os.getenv("TBANK_SANDBOX_TOKEN")
        self.url = os.getenv("TBANK_URL_PROD")
        self.sandbox_url = os.getenv("TBANK_URL_SANDBOX")

    def __repr__(self):
        return f"Бот для поиска первых импульсов дня"

    async def start_bot(self):
        """Запуск бота"""
        logging.info("Start bot...")

        shares = await self.get_shares(self.sandbox_token, INVEST_GRPC_API)
        logger.info(shares)

    @staticmethod
    async def end_bot():
        """Остановка бота"""
        logging.info("End bot...")