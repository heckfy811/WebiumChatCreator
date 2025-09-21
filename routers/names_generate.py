from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from parsers import get_students, get_course
from states.states import Course
from db import db
from keyboards import kb

router = Router()
@router.message(F.text == "Сгенерить все названия")
async def set_course(message: Message, state: FSMContext):
    await message.answer(text="Введите ID курса:")
    await state.set_state(Course.course_id)

@router.message(Course.course_id)
async def give_names(message: Message, state: FSMContext):
    await state.update_data(course_id=message.text)
    data = await state.get_data()
    mentor = db.get_mentor(message.from_user.id)
    #TODO: убрать эту ебанину с цифрами
    mentor_name = mentor[2]
    token = mentor[3]
    try:
        students = get_students.get_students(data["course_id"], token)
        course_name = get_course.get_course_name(data["course_id"], token)
    except TypeError:
        await message.answer(text="Курс не существует или у Вас недостаточно прав.")
        return
    await message.answer(text="да начнется щитпост")
    for i in range(len(students)):
        await message.answer(text=f"{mentor_name} — {students[i]}. {course_name}.")
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)