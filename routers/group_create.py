from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from states.group_name import GroupName
from db import db
from keyboards import kb

router = Router()
@router.message(F.text == "Создать группу")
async def start_form(message: Message, state: FSMContext):
    await message.answer(text="Введите имя ученика:")
    await state.set_state(GroupName.student_name)

@router.message(GroupName.student_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(student_name=message.text)
    await message.answer("Выберите продукт: ", reply_markup=kb.product_kb)
    await state.set_state(GroupName.product)

@router.message(GroupName.product)
async def process_product(message: Message, state: FSMContext):
    await state.update_data(product=message.text)
    await message.answer("Выберите месяц обучения: ", reply_markup=kb.month_kb)
    await state.set_state(GroupName.month)

@router.message(GroupName.month)
async def process_month(message: Message, state: FSMContext):
    await state.update_data(month=message.text)
    data = await state.get_data()
    tutor_name = db.get_mentor(message.from_user.id)
    group_name = (f"{tutor_name} — {data['student_name']}. Информатика. "
                  f"{data['product']}. {data['month']}ский поток подготовки к ЕГЭ 2026.")
    await message.answer(f"Готовое название:\n{group_name}")