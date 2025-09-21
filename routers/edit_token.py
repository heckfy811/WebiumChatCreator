from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from states.states import Token
from db import db
from keyboards import kb

router = Router()
@router.message(F.text == "Изменить токен")
async def set_token(message: Message, state: FSMContext):
    await message.answer(text="Введите новый токен:")
    await state.set_state(Token.refresh_token)

@router.message(Token.refresh_token)
async def set_token(message: Message, state: FSMContext):
    await state.update_data(refresh_token=message.text)
    mentor_name = db.get_mentor(message.from_user.id)
    db.save_mentor(message.from_user.id, mentor_name, message.text)
    await message.answer(text="Токен успешно изменен :3")
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)