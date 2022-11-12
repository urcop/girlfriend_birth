from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from data.config import BASE_DIR, TEXT_FOR_CONGRATULATIONS
from keyboards.inline.congratulations import keyboard, back_video_keyboard
from loader import dp


@dp.message_handler(Command(['congratulations']))
async def congratulations(message: types.Message, page: int = 3):
    await message.answer(text=TEXT_FOR_CONGRATULATIONS,
                         reply_markup=keyboard(page))


@dp.callback_query_handler(text_contains='page_')
async def pagination(call: types.CallbackQuery):
    await call.message.delete()
    data = call.data

    action = data.split('_')[1]
    page = int(data.split('_')[2])
    if action == 'next':
        page = page + 3
    else:
        page = page - 3

    await call.message.answer(text=TEXT_FOR_CONGRATULATIONS,
                              reply_markup=keyboard(page))


@dp.callback_query_handler(text_contains='congratulate_')
async def videos(call: types.CallbackQuery):
    await call.message.delete()
    data = call.data
    video_name = data.split('_')[1]
    video = InputFile(BASE_DIR / 'data' / 'videos' / video_name)
    await call.message.answer_video(video, reply_markup=back_video_keyboard, width=720, height=1280)


@dp.callback_query_handler(text_contains='back_to_videos')
async def back_to_videos(call: types.CallbackQuery):
    await call.message.delete()
    await congratulations(call.message)
