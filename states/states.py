from aiogram.fsm.state import State, StatesGroup

class Course(StatesGroup):
    course_id = State()

class Mentor(StatesGroup):
    mentor_name = State()