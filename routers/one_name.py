from aiogram.types import Message, FSInputFile, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from parsers import get_students, get_course
from states.states import Student
from db import db
from keyboards import kb

router = Router()
@router.message(F.text == "Сгенерить одно название")
async def set_course(message: Message, state: FSMContext):
    image = FSInputFile("static/course_id.png")
    await message.answer_photo(image, caption="Введите ID курса (зайди на курс в админке и скопируй циферки там):")
    await state.set_state(Student.course_id)

@router.message(Student.course_id)
async def set_student(message: Message, state: FSMContext):
    image_1 = InputMediaPhoto(type='photo', media=FSInputFile("static/student_id_1.png"), caption="Введите ID студента:\n"
                              "1. Уменьши страницу с курсом по горизонтали, чтобы она приобрела подобный вид\n"
                              "2. Зайди на нужного ученика\n"
                              "3. Скопируй ID из ссылки")
    image_2 = InputMediaPhoto(type='photo', media=FSInputFile("static/student_id_2.png"))
    media = [image_1, image_2]
    await state.update_data(course_id=message.text)
    await message.answer_media_group(media=media)
    await state.set_state(Student.student_id)

@router.message(Student.student_id)
async def generate_name(message: Message, state: FSMContext):
    await state.update_data(student_id=message.text)
    mentor = db.get_mentor(message.from_user.id)
    tutor_name = mentor[2]
    token = mentor[3]
    data = await state.get_data()
    try:
        course_name = get_course.get_course_name(data["course_id"], token)
    except TypeError:
        await message.answer(text="Курс не существует или у Вас недостаточно прав.")
        return
    try:
        student_name = get_students.get_student_by_id(data["course_id"], data["student_id"], token)
    except TypeError:
        await message.answer(text="Ученик не существует или у Вас недостаточно прав.")
        return
    await message.answer(text=f"{tutor_name} — {student_name}. {course_name}.")
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=kb.start_kb)