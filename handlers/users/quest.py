from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.check_right_answer import check, answers
from data.config import PLACE1_ANSWER, PLACE2_ANSWER, PLACE3_ANSWER, PLACE4_ANSWER, PLACE5_ANSWER
from data.start_quest import check_available
from keyboards.inline.quest import quest_start_keyboard
from loader import dp
from states.quest import Quest


@dp.message_handler(Command(['quest']))
async def quest(message: types.Message):
    if not check_available():
        await message.answer('Пока рано, квест доступен только с 13:00 (чтобы ты не тыкала все подряд раньше времени) ')
    else:
        await message.answer('сайт для поиска по кордам - https://geotree.ru/coordinates',
                             disable_web_page_preview=True)
        await message.answer(
            text='Квест начался, суть квеста:\n\n'
                 '\t\t1. Ты должна будешь искать по координатам листочки и на них написано '
                 'что писать в бота чтобы пройти дальше\n'
                 '\t\t2. С тобой буду ходить я (потому что я знаю что ты можешь не '
                 'найти или не увидеть)\n'
                 '\t\t3. Жульничать, искать обходные какие либо пути, подкупать меня - нельзя\n',
            reply_markup=quest_start_keyboard,
            disable_web_page_preview=True)


@dp.callback_query_handler(text='start_quest')
async def start_quest(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Первые координаты - <code>43.399899, 39.979807</code>')
    await sleep(3)
    await call.message.answer('Вводи слово которое нашла')
    await Quest.place1.set()


@dp.message_handler(state=Quest.place1)
async def place1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place1'] = message.text
        if check(data['place1'], PLACE1_ANSWER):
            await message.answer(text=answers('good'))
            await message.answer('Некст координаты - <code>43.400923, 39.980339</code>')
            await sleep(3)
            await message.answer('Следующее слово')
            await Quest.next()
        else:
            await message.answer(text=answers('wrong'))
            await Quest.place1.set()


@dp.message_handler(state=Quest.place2)
async def place2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place2'] = message.text
        if check(data['place2'], PLACE2_ANSWER):
            await message.answer(text=answers('good'))
            await message.answer('Сюда - <code>43.401728, 39.979220</code>')
            await sleep(3)
            await message.answer('че там написано?')
            await Quest.next()
        else:
            await message.answer(text=answers('wrong'))
            await Quest.place2.set()


@dp.message_handler(state=Quest.place3)
async def place3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place3'] = message.text
        if check(data['place3'], PLACE3_ANSWER):
            await message.answer(text=answers('good'))
            await message.answer('Щас сюда - <code>43.401598, 39.981340</code>')
            await sleep(3)
            await message.answer('что некст?')
            await Quest.next()
        else:
            await message.answer(text=answers('wrong'))
            await Quest.place3.set()


@dp.message_handler(state=Quest.place4)
async def place4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place4'] = message.text
        if check(data['place4'], PLACE4_ANSWER):
            await message.answer(text=answers('good'))
            await message.answer('вот сюда теперь - <code>43.401372, 39.980916</code>')
            await sleep(15)
            await message.answer('думаю догадалась что мне от тебя надо')
            await Quest.next()
        else:
            await message.answer(text=answers('wrong'))
            await Quest.place4.set()


@dp.message_handler(state=Quest.place5)
async def place4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['place5'] = message.text
        if check(data['place5'], PLACE5_ANSWER):
            await message.answer('Ты прошла квест, про подарок спрашивай у керила я нихуя не знаю🤪🤪🤪🤪')
            await state.finish()
        else:
            await message.answer(text=answers('wrong'))
            await Quest.place5.set()
