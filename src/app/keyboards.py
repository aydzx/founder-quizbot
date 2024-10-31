from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for option in answer_options:
        builder.add(
            InlineKeyboardButton(
                text=option,
                callback_data=(
                    "right_answer" if option == right_answer else "wrong_answer"
                ),
            )
        )

    builder.adjust(1)
    return builder.as_markup()


def generate_start_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Начать игру"))
    builder.add(KeyboardButton(text="Посмотреть статистику"))

    return builder
