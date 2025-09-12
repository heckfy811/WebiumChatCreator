from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

import parser
from states.states import Student
from db import db
from keyboards import kb

router = Router()
@router.message(F.text == "Сгенерить одно название")
async def set_course(message: Message, state: FSMContext):
    await message.answer(text="Введите ID курса:")
    await state.set_state(Student.course_id)

@router.message(Student.course_id)
async def set_student(message: Message, state: FSMContext):
    await state.update_data(course_id=message.text)
    await message.answer(text="Введите ID студента:")
    await state.set_state(Student.student_id)

@router.message(Student.student_id)
async def generate_name(message: Message, state: FSMContext):
    await state.update_data(student_id=message.text)
    data = await state.get_data()
    try:
        course_name = parser.get_course_name(data["course_id"])
    except TypeError:
        await message.answer(text="Курс не существует или у Вас недостаточно прав.")
        return
    try:
        student_name = parser.get_student_by_id(data["course_id"], data["student_id"])
    except TypeError:
        await message.answer(text="Ученик не существует или у Вас недостаточно прав.")
        return
    tutor_name = db.get_mentor(message.from_user.id)[2]
    await message.answer(text=f"{tutor_name} — {student_name}. {course_name}.")
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)