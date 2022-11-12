from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')  # Забираем значение типа str
ADMINS = env.list('ADMINS')  # Тут у нас будет список из админов
IP = env.str('ip')  # Тоже str, но для айпи адреса хоста

BASE_DIR = Path(__file__).resolve().parent.parent  # Корневая папка проекта

TEXT_FOR_CONGRATULATIONS = env.str(
    'TEXT_FOR_CONGRATULATIONS'
)  # Текст, который выводится после команды /congratulations
# START_TEXT = env.str('START_TEXT')  # Текст, который выводится после команды /start

DEBUG = env.int('DEBUG')

PLACE1_ANSWER = env.str('PLACE1_ANSWER')
PLACE2_ANSWER = env.str('PLACE2_ANSWER')
PLACE3_ANSWER = env.str('PLACE3_ANSWER')
PLACE4_ANSWER = env.str('PLACE4_ANSWER')
PLACE5_ANSWER = env.str('PLACE5_ANSWER')