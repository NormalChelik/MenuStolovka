import asyncio
import json

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from routers.commands import command_router
from routers.callbacks import callback_router

from db.create_db import create_tables
from db.sessions.menu_session import add_dish, check_dish_by_name

config_INFO = json.load(open("bot_config.json", "r"))
menu_file = [i for i in open("menu.txt").read().split("\n") if i]


# Главная функция, запускает бота
async def main() -> None:
    create_tables()

    for i in range(0, len(menu_file), 2):
        if not check_dish_by_name(menu_file[i]):
            add_dish(name_dish=menu_file[i],
                     descripton_dish=menu_file[i + 1],
                     photo_id="0")

    bot = Bot(token=config_INFO["token"], parse_mode="HTML")

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(command_router, callback_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())