from aiogram.fsm.state import StatesGroup, State

class MenuStates(StatesGroup):
    name_dish_state = State()
    description_dish_state = State()
    photo_dish_state = State()