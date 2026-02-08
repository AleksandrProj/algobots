import logging
import asyncio

import aiohttp

from app.bots.impulse_day_bot.controllers import Bot


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',)

    await start_bot()

async def start_bot():
    """Запуск бота"""
    async with aiohttp.ClientSession() as session:
        await impulse_day_bot(session)

async def impulse_day_bot(session: aiohttp.ClientSession = None):
    """Бот: Первый импульс дня"""
    bot = Bot(
        session_bot=session,
    )

    await bot.start_bot()
    await bot.end_bot()


if __name__ == "__main__":
    asyncio.run(main())
