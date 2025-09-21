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
    #проверяем на наличие имени и токена в базе
    mentor = db.get_mentor(message.from_user.id)
    if mentor:
        await message.answer(text=f"С возвращением, {mentor[2]}! 🚀")
        await message.answer("Выберите действие:", reply_markup=kb.start_kb)
    else:
        await message.answer(text="Привет! Введи своё имя:")
        await state.set_state(Mentor.mentor_name)

@router.message(Mentor.mentor_name)
async def set_mentor_name(message: Message, state: FSMContext):
    await state.update_data(mentor_name=message.text)
    await message.answer(text="Введи свой JWT-токен")
    await state.set_state(Mentor.refresh_token)

@router.message(Mentor.refresh_token)
async def set_mentor_token(message: Message, state: FSMContext):
    await state.update_data(refresh_token=message.text)
    data = await state.get_data()
    print(data)
    db.save_mentor(message.from_user.id, data["mentor_name"] ,message.text)
    await message.answer(f"Спасибо, {data["mentor_name"]}! Теперь я все запомнил ✨")
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)