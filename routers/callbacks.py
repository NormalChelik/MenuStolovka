from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery

from keyboards.kb import create_score_kb

from db.sessions.menu_session import check_dish, check_dish_by_name
from db.sessions.score_menu_session import add_score, check_user_score, check_dish_score

callback_router = Router()

@callback_router.callback_query()
async def click_dish(clbq: CallbackQuery, bot: Bot):
    if clbq.data in [k[0] for k in check_dish()]:
        if not check_user_score(clbq.from_user.id, clbq.data):
            await bot.send_message(chat_id=clbq.from_user.id,
                                 text=f"<b>Название блюда:</b> {clbq.data}\n\n<b>Описание блюда:</b> {check_dish_by_name(clbq.data)[0]}\n<b>Оценка:</b> {check_count_score(clbq.data)}/10",
                                 reply_markup=create_score_kb(clbq.data))
        else:
            await bot.send_message(chat_id=clbq.from_user.id,
                                 text=f"<b>Название блюда:</b> {clbq.data}\n\n<b>Описание блюда:</b> {check_dish_by_name(clbq.data)[0]}\n<b>Оценка:</b> {check_count_score(clbq.data)}/10")

    if clbq.data in [f"score_{i}_{k[0]}" for k in check_dish() for i in range(11)]:
        add_score(user_id=clbq.from_user.id,
                  name_dish=clbq.data.split("_")[2],
                  score=int(clbq.data.split("_")[1]))

        await clbq.message.edit_text(
              text=f"<b>Название блюда:</b> {clbq.data.split('_')[2]}\n\n<b>Описание блюда:</b> {check_dish_by_name(clbq.data.split('_')[2])[0]}\n<b>Оценка:</b> {check_count_score(clbq.data.split('_')[2])}/10",
              reply_markup=None)

def check_count_score(dish):
    if len(check_dish_score(dish)) > 0:
        return sum([s[0] for s in check_dish_score(dish)]) / len(check_dish_score(dish))
    else:
        return 0