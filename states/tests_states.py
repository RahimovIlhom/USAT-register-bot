from aiogram.dispatcher.filters.state import State, StatesGroup


class AddQuestionTestStatesGroup(StatesGroup):
    science = State()
    test = State()
    update = State()
    image = State()
    question = State()


class CreateTestStatesGroup(StatesGroup):
    science = State()
    language = State()
    count = State()
