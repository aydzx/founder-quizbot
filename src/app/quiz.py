from app.keyboards import generate_options_keyboard
import app.db as db
from app.questions import get_data

quiz_data = get_data()


async def get_question(message, user_id):
    # Получение текущего вопроса из словаря состояний пользователя
    current_question_index = await db.get_quiz_index(user_id)
    correct_index = quiz_data[current_question_index]["correct_option"]
    opts = quiz_data[current_question_index]["options"]
    kb = generate_options_keyboard(opts, opts[correct_index])
    await message.answer(
        f"{quiz_data[current_question_index]['question']}", reply_markup=kb
    )


async def new_quiz(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    current_question_index = 0
    await db.update_quiz_index(user_id, user_name, current_question_index)
    await get_question(message, user_id)
