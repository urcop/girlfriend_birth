from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

quest_start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Начать🤪', callback_data='start_quest')
        ]
    ]
)