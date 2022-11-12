from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import BASE_DIR
from data.get_files import get_files


def keyboard(page: int = 3):
    videos_path = BASE_DIR / 'data' / 'videos'
    videos = get_files(videos_path)

    max_pages = len(videos) + 3

    next_page = page + 3
    next_page_text = 'Далее ➡️'

    previous_page = page - 3
    previous_page_text = '⬅ Назад️'

    markup = InlineKeyboardMarkup(row_width=2)

    for video in videos[page - 3:page]:
        file_name = video[1].split('.')[0]
        btn = InlineKeyboardButton(text=f'{file_name}',
                                   callback_data=f'congratulate_{video[1]}')
        markup.add(btn)

    previous_btn = InlineKeyboardButton(text=previous_page_text, callback_data=f'page_back_{page}')
    next_btn = InlineKeyboardButton(text=next_page_text, callback_data=f'page_next_{page}')

    if next_page <= max_pages and previous_page > 0:
        markup.add(previous_btn)
        markup.insert(next_btn)
    elif next_page <= max_pages:
        markup.add(next_btn)
    elif previous_page > 0:
        markup.add(previous_btn)

    return markup


back_video_keyboard = InlineKeyboardMarkup(row_width=1)
back_video_keyboard.add(InlineKeyboardButton('⬅ Назад️', callback_data='back_to_videos'))
