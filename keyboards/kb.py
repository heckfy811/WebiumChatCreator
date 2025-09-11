from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

#кнопочки
start = [[KeyboardButton(text="Сгенерить названия")]]

start_kb = ReplyKeyboardMarkup(keyboard=start, resize_keyboard=True, one_time_keyboard=True)

