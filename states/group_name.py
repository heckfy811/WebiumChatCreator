from aiogram.fsm.state import State, StatesGroup

class GroupName(StatesGroup):
    mentor_name = State()
    student_name = State()
    product = State()
    month = State()