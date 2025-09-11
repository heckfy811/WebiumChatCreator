from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

import parser
from states.states import Course
from db import db

router = Router()
@router.message(F.text == "Сгенерить названия")
async def set_course(message: Message, state: FSMContext):
    await message.answer(text="Введите ID курса:")
    await state.set_state(Course.course_id)

@router.message(Course.course_id)
async def give_names(message: Message, state: FSMContext):
    await state.update_data(course_id=message.text)
    data = await state.get_data()
    try:
        course_name, students = parser.get_students(data["course_id"])
    except TypeError:
        await message.answer(text="Курс не существует или у Вас недостаточно прав.")
        return
    tutor_name = db.get_mentor(message.from_user.id)
    await message.answer(text="да начнется щитпост")
    for i in range(len(students)):
        await message.answer(text=f"{tutor_name} — {students[i]}. {course_name}.")