# @title Полный код бота для самоконтроля
import asyncio
import logging
from aiogram import Bot, Dispatcher

import app.db as db
from app.handlers import router

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = "6490996410:AAEc1HfwshFbpptICd5AV1BGR6Txo4OtDgE"

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()
# подключаем router
dp.include_router(router)


# Запуск процесса поллинга новых апдейтов
async def main():
    # Запускаем создание таблицы базы данных
    await db.create_table()

    await dp.start_polling(bot)


if __name__ == "__main__":
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
