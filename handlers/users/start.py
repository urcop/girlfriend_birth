from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        'Привет, моя золотая, короче как клевый подарок я написал бота, если скажешь хуйня я тебя сьем...😍\n'
        'так вот.. тут остались команды с бота который я писал тебе в электричке, и добавил немного кайфа👉👈\n'
        'чекай меню и тыкай по командам(меню если че снизу слева)↙️')
