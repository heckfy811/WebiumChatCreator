from aiogram.types import KeyboardButton
from aiogram.types import Message, ReplyKeyboardMarkup

#кнопочки
start = [[KeyboardButton(text="Создать группу")]]

product = [[KeyboardButton(text="Основа")],
           [KeyboardButton(text="Плюс")]]

month = [[KeyboardButton(text="Сентябрь")],
         [KeyboardButton(text="Октябрь")],
         [KeyboardButton(text="Ноябрь")],
         [KeyboardButton(text="Декабрь")],
         [KeyboardButton(text="Январь")],
         [KeyboardButton(text="Февраль")],
         [KeyboardButton(text="Март")],
         [KeyboardButton(text="Апрель")],
         [KeyboardButton(text="Май")]]

start_kb = ReplyKeyboardMarkup(keyboard=start, resize_keyboard=True, one_time_keyboard=True)
product_kb = ReplyKeyboardMarkup(keyboard=product, resize_keyboard=True, one_time_keyboard=True)
month_kb = ReplyKeyboardMarkup(keyboard=month, resize_keyboard=True, one_time_keyboard=True)

