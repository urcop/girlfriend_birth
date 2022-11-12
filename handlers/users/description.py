from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command(["description"]))
async def description(message: types.Message):
    text = [
        'Виола самая лучшая девочка в сочи, если бы не она не было бы Путина, и не создали бы сириус',
        'всегда на приколе и даже немного дурная моментами да, но все равно самая лучшая',
        'тот кто пишет это дерьмо не умеет подбирать слов, но Леля самая лучшая это факт'
    ]
    await message.answer('\n'.join(text))
    await message.answer_sticker('CAACAgIAAxkBAAMWYwYn8fDH5iG3gj8crVv-TW1d89UAAiIVAAICy_lL5LQRn6pHkn8pBA')
