from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from states.states import Token
from db import db
from keyboards import kb

router = Router()
@router.message(F.text == "Изменить токен")
async def set_token(message: Message, state: FSMContext):
    photo = FSInputFile("static/token.png")
    await message.answer_photo(photo, caption="Напоминалочка\n"
                                              "1. Зайди на страницу курса в админке\n"
                                              "2. Нажми F12\n"
                                              "3. В появившейся панельке нажми на вкладку Network\n"
                                              "4. Выбери Fetch/XHR\n"
                                              "5. Обнови страницу\n"
                                              "6. Выбери запрос me/\n"
                                              "7. В Headers пролистай ниже, скопируй значение Authorization после 'Bearer' и кинь сюда\n")
    await state.set_state(Token.refresh_token)

@router.message(Token.refresh_token)
async def set_token(message: Message, state: FSMContext):
    await state.update_data(refresh_token=message.text)
    mentor_name = db.get_mentor(message.from_user.id)[2]
    db.save_mentor(message.from_user.id, mentor_name, message.text)
    await message.answer(text="Токен успешно изменен :3")
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)