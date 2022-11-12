from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import START_TEXT
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(START_TEXT)
