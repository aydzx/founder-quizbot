from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for i, option in enumerate(answer_options):
        # print(f"right_answer_{option}".encode().decode() if option == right_answer else f"wrong_answer_{option}".encode().decode())
        builder.add(
            InlineKeyboardButton(
                text=option,
                callback_data=(
                    f"right_answer_{i}"
                    if option == right_answer
                    else f"wrong_answer_{i}"
                ),
            )
        )

    builder.adjust(1)
    return builder.as_markup()


def generate_start_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Начать игру"))
    builder.add(KeyboardButton(text="Посмотреть статистику"))
    # builder.adjust(1)

    return builder
