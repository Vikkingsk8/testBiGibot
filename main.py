# #Use this token to access the HTTP API:
# 6147694776:AAEpPG7Z5C5YzR7ipZMcBW9CNYt5QvCxqqM
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
# Здесь запускается бот


from aiogram import Bot, Dispatcher
import logging
import asyncio
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router

dp = Dispatcher()


async def main():
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
