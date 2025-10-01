from aiogram.filters import CommandStart
from aiogram import Router

from aiogram.fsm.context import FSMContext

from aiogram.types import Message, FSInputFile

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
        await message.answer(text="Привет! Я - бот для создания названий для бесед с учениками\n\nВведи своё имя (как будет в названиях групп):")
        await state.set_state(Mentor.mentor_name)

@router.message(Mentor.mentor_name)
async def set_mentor_name(message: Message, state: FSMContext):
    photo = FSInputFile("static/token.png")
    await state.update_data(mentor_name=message.text)
    await message.answer_photo(photo, caption="Сейчас будет сложно, но ты справишься, я верю\n"
                                              "1. Зайди на страницу курса в админке\n"
                                              "2. Нажми F12\n"
                                              "3. В появившейся панельке нажми на вкладку Network\n"
                                              "4. Выбери Fetch/XHR\n"
                                              "5. Обнови страницу\n"
                                              "6. Выбери запрос me/\n"
                                              "7. В Headers пролистай ниже, скопируй значение Authorization после 'Bearer' и кинь сюда")
    await state.set_state(Mentor.refresh_token)

@router.message(Mentor.refresh_token)
async def set_mentor_token(message: Message, state: FSMContext):
    await state.update_data(refresh_token=message.text)
    data = await state.get_data()
    db.save_mentor(message.from_user.id, data["mentor_name"] ,message.text)
    await message.answer(f"Спасибо, {data["mentor_name"]}! Теперь я все запомнил ✨")
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)