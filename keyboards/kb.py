from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.sessions.menu_session import check_dish

def create_menu_kb():
    builder = InlineKeyboardBuilder()

    for k in check_dish():
        builder.button(text=k[0], callback_data=k[0])

    builder.adjust(2)

    return builder.as_markup()

def create_score_kb(name_dish: str):
    builder = InlineKeyboardBuilder()

    for i in range(0, 11):
        builder.button(text=str(i), callback_data=f"score_{i}_{name_dish}")

    builder.adjust(5)

    return builder.as_markup()



