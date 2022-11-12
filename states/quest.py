from aiogram.dispatcher.filters.state import StatesGroup, State


class Quest(StatesGroup):
    place1 = State()
    place2 = State()
    place3 = State()
    place4 = State()
    place5 = State()