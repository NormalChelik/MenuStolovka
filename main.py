import asyncio
import json

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from routers.commands import command_router
from routers.callbacks import callback_router

from db.create_db import create_tables

config_INFO = json.load(open("bot_config.json", "r"))


# Главная функция, запускает бота
async def main() -> None:
    create_tables()

    bot = Bot(token=config_INFO["token"], parse_mode="HTML")

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(command_router, callback_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())