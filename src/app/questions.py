# Структура квиза
quiz_data = [
    {
        "question": "Что такое Python?",
        "options": [
            "Язык программирования",
            "Тип данных",
            "Музыкальный инструмент",
            "Змея на английском",
        ],
        "correct_option": 0,
    },
    {
        "question": "Какой тип данных используется для хранения целых чисел?",
        "options": ["int", "float", "str", "natural"],
        "correct_option": 0,
    },
    {
        "question": "Какой тип данных используется для хранения вещественных чисел?",
        "options": ["int", "float", "str", "natural"],
        "correct_option": 1,
    },
    {
        "question": "Какой тип данных используется для хранения строк?",
        "options": ["int", "float", "str", "natural"],
        "correct_option": 2,
    },
    {
        "question": "Что такое GIL?",
        "options": [
            "Глобальная разблокировка интерпретатора",
            "Глобальная блокировка интерпретатора",
            "Не знаю",
            "Аббревиатура",
            "Блокировка доступа к памяти",
        ],
        "correct_option": 1,
    },
    {
        "question": "Выберите фреймворк Python",
        "options": ["Spring", "Node", "QtCreator", "Django"],
        "correct_option": 3,
    },
    {
        "question": "Как переводится dependency?",
        "options": ["Возможность", "Зависимость", "Данные", "Последовательность"],
        "correct_option": 1,
    },
    {
        "question": "Есть ли в Python функция map()?",
        "options": ["Да", "Нет"],
        "correct_option": 0,
    },
    {
        "question": "Какая основная функция в Python?",
        "options": ["general()", "main()", "start()", "go()"],
        "correct_option": 1,
    },
    {
        "question": "Тебе нравится программировать?",
        "options": ["Нет", "Да"],
        "correct_option": 1,
    },
]


def get_data():
    return quiz_data
