from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters.command import Command

from app.keyboards import generate_start_keyboard

from app.quiz import new_quiz
from app.utils import *


router = Router()


@router.callback_query(F.data.startswith("right_answer"))
async def right_answer(callback: CallbackQuery):

    await edit_message(callback)

    await send_answer(callback)

    await callback.message.answer("Верно!")

    await update_current_index(callback)

    await update_current_score(callback)

    await check_answer(callback, len(quiz_data))


@router.callback_query(F.data.startswith("wrong_answer"))
async def wrong_answer(callback: CallbackQuery):

    await edit_message(callback)

    correct_option = await get_correct_option(callback)

    await send_answer(callback)

    await callback.message.answer(f"Неправильно. Правильный ответ: {correct_option}")

    await update_current_index(callback)

    await check_answer(callback, len(quiz_data))


# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    builder = generate_start_keyboard()
    await message.answer(
        "Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True)
    )


# Хэндлер на команду /quiz
@router.message(F.text == "Начать игру")
@router.message(Command("quiz"))
async def cmd_quiz(message: Message):

    await message.answer(f"Давайте начнем квиз!")
    await new_quiz(message)


# Хэндлер на команду /statistics
@router.message(F.text == "Посмотреть статистику")
@router.message(Command("statistics"))
async def cmd_statistics(message: Message):
    statistics = await get_statistics()

    await message.answer(statistics)
    # await new_quiz(message)
