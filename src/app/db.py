import aiosqlite

# Зададим имя базы данных
DB_NAME = "quiz_bot.db"


async def get_quiz_index(user_id):
    # Подключаемся к базе данных
    async with aiosqlite.connect(DB_NAME) as db:
        # Получаем запись для заданного пользователя
        async with db.execute(
            "SELECT question_index FROM quiz_state WHERE user_id = (?)", (user_id,)
        ) as cursor:
            # Возвращаем результат
            results = await cursor.fetchone()
            if results is not None:
                return results[0]
            else:
                return 0


async def update_quiz_index(user_id, user_name, index, max_score = 0):
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Вставляем новую запись или заменяем ее, если с данным user_id уже существует
        await db.execute(
            "INSERT OR REPLACE INTO quiz_state (user_id, user_name, question_index, max_score) VALUES (?, ?, ?, ?)",
            (user_id, user_name, index, max_score),
        )
        # Сохраняем изменения
        await db.commit()


async def get_max_score(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT max_score FROM quiz_state WHERE user_id = (?)", (user_id,)
        ) as cursor:
            results = await cursor.fetchone()
            if results is not None:
                return results[0]
            else:
                return 0
            

async def get_users_max_score():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT user_name, max_score FROM quiz_state"
        ) as cursor:
            results = await cursor.fetchall()
            if results is not None:
                return results
            else:
                return None


async def update_max_score(user_id, score):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE quiz_state SET max_score = (?) WHERE user_id = (?)",
            (score, user_id),
        )

        await db.commit()
    
    


async def create_table():
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Создаем таблицу
        await db.execute(
            """CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, user_name VARCHAR, question_index INTEGER DEFAULT 0, max_score INTEGER DEFAULT 0)"""
        )
        # Сохраняем изменения
        await db.commit()
