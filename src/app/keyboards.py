from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for option in answer_options:
        builder.add(
            InlineKeyboardButton(
                text=option,
                callback_data=(
                    f"right_answer_{option}"
                    if option == right_answer
                    else f"wrong_answer_{option}"
                ),
            )
        )

    builder.adjust(1)
    return builder.as_markup()


def generate_start_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Начать игру"))
    builder.add(KeyboardButton(text="Посмотреть статистику"))
    builder.adjust(1)

    return builder
