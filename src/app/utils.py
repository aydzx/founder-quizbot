import app.db as db
from app.quiz import *


async def update_current_index(callback):
    current_question_index = await db.get_quiz_index(callback.from_user.id)
    current_question_index += 1
    max_score = await db.get_max_score(callback.from_user.id)
    await db.update_quiz_index(callback.from_user.id, callback.from_user.username, current_question_index, max_score)


async def check_answer(callback, length_data):
    current_question_index = await db.get_quiz_index(callback.from_user.id)
    if current_question_index < length_data:
        await get_question(callback.message, callback.from_user.id)
    else:
        await callback.message.answer("Это был последний вопрос. Квиз завершен!")


async def get_correct_option(callback):
    # Получение текущего вопроса из словаря состояний пользователя
    current_question_index = await db.get_quiz_index(callback.from_user.id)
    correct_option = quiz_data[current_question_index]["correct_option"]
    return quiz_data[current_question_index]["options"][correct_option]


async def edit_message(callback):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None,
    )

async def update_current_score(callback):
    current_score = await db.get_max_score(callback.from_user.id) 
    current_score += 1
    await db.update_max_score(callback.from_user.id, current_score)

async def get_statistics():
    users = await db.get_users_max_score()

    statistics = ''

    for user_name, score in users:
        statistics += f'{user_name} \t| {score} \n'
    
    return statistics
