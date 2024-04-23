from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command

from states.menu_states import MenuStates

from keyboards.kb import create_menu_kb

from db.sessions.menu_session import add_dish

command_router = Router()

@command_router.message(Command("start"))
async def start(message: Message):
    await message.answer(text=f"Добро пожаловать в меню нашей столовой! Здесь вы можете посмотреть меню и поставить оценку каждому блюду.\nВведите команду /menu.")

@command_router.message(Command("addDish"))
async def start(message: Message, state: FSMContext):
    await message.answer(text=f"Введите название блюда:")
    await state.set_state(MenuStates.name_dish_state)

@command_router.message(MenuStates.name_dish_state)
async def input_name_dish(message: Message, state: FSMContext):
    await message.answer("Введите описание для блюда:")
    await state.update_data(name_dish_state=message.text)
    await state.set_state(MenuStates.description_dish_state)

@command_router.message(MenuStates.description_dish_state)
async def input_description_dish(message: Message, state: FSMContext):
    await message.answer("Выберите фото для блюда:")
    await state.update_data(description_dish_state=message.text)
    await state.set_state(MenuStates.photo_dish_state)

@command_router.message(MenuStates.photo_dish_state)
async def input_photo_dish(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(photo_dish_state=message.photo[0].file_id)
    data = await state.get_data()

    add_dish(name_dish=data['name_dish_state'],
             descripton_dish=data['description_dish_state'],
             photo_id=data["photo_dish_state"])

    await bot.send_photo(chat_id=message.chat.id,
                         photo=data["photo_dish_state"],
                         caption=f"*Название блюда:* {data['name_dish_state']}\n\n*Описание блюда:* {data['description_dish_state']}")

    await state.clear()

@command_router.message(Command("menu"))
async def menu(message: Message):
    await message.answer(text=f"*МЕНЮ СТОЛОВОЙ МИИТ*", reply_markup=create_menu_kb())