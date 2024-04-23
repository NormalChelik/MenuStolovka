from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery

from keyboards.kb import create_score_kb

from db.sessions.menu_session import check_dish, check_dish_by_name
from db.sessions.score_menu_session import add_score, check_user_score, check_dish_score

callback_router = Router()

@callback_router.callback_query(F.data.in_([k[0] for k in check_dish()]))
async def click_dish(clbq: CallbackQuery, bot: Bot):
    if not check_user_score(clbq.from_user.id, clbq.data):
        print(check_dish_score(clbq.data))
        await bot.send_photo(chat_id=clbq.from_user.id,
                             photo=check_dish_by_name(clbq.data)[1],
                             caption=f"*Название блюда:* {clbq.data}\n\n*Описание блюда:* {check_dish_by_name(clbq.data)[0]}\n*Оценка:* _{check_count_score(clbq.data)}/10_",
                             reply_markup=create_score_kb(clbq.data))
    else:
        await bot.send_photo(chat_id=clbq.from_user.id,
                             photo=check_dish_by_name(clbq.data)[1],
                             caption=f"*Название блюда:* {clbq.data}\n\n*Описание блюда:* {check_dish_by_name(clbq.data)[0]}\n*Оценка:* _{check_count_score(clbq.data)}/10_")

@callback_router.callback_query(F.data.in_([f"score_{i}_{k[0]}" for k in check_dish() for i in range(11)]))
async def save_score_by_dish(clbq: CallbackQuery):
    add_score(user_id=clbq.from_user.id,
              name_dish=clbq.data.split("_")[2],
              score=int(clbq.data.split("_")[1]))

    await clbq.message.edit_caption(caption=f"*Название блюда:* {clbq.data.split('_')[2]}\n\n*Описание блюда:* {check_dish_by_name(clbq.data.split('_')[2])[0]}\n*Оценка:* _{check_count_score(clbq.data.split('_')[2])}/10_",
                                    reply_markup=None)

def check_count_score(dish):
    if len(check_dish_score(dish)) > 0:
        print(check_dish_score(dish))
        return sum([s[0] for s in check_dish_score(dish)]) / len(check_dish_score(dish))
    else:
        return 0