from random import choice

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from data.config import BASE_DIR
from data.get_files import get_files
from loader import dp


@dp.message_handler(Command(['who_is_best']))
async def who_is_best(message: types.Message):
    photo_path = BASE_DIR / 'data' / 'photos'
    photos = get_files(photo_path)
    variants = ['уебан', 'гнида ебаная', 'пошел нахуй', 'черт сука']

    shuffle_result = choice([f'{photo[0]}/{photo[1]}' for photo in photos])

    result = InputFile(shuffle_result)
    await message.answer(f'Она. Она самая лучшая, кто так не считает тот {choice(variants)}')
    await message.answer_photo(photo=result)
