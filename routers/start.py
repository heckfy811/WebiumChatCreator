from aiogram.filters import CommandStart
from aiogram import Router

from aiogram.fsm.context import FSMContext

from aiogram.types import Message

from keyboards import kb
from db import db
from states.states import Mentor

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    #проверяем на наличие имени в базе
    mentor_name = db.get_mentor(message.from_user.id)
    if mentor_name:
        await message.answer(text=f"С возвращением, {mentor_name}! 🚀")
        await message.answer("Выберите действие:", reply_markup=kb.start_kb)
    else:
        await message.answer(text="Привет! Введи своё имя:")
        await state.set_state(Mentor.mentor_name)

@router.message(Mentor.mentor_name)
async def set_mentor_name(message: Message, state: FSMContext):
    db.save_mentor(message.from_user.id, message.text)
    await message.answer(f"Спасибо, {message.text}! Теперь я запомнил твоё имя ✨")
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)