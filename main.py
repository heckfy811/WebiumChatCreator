import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from routers import start, names_generate, one_name, edit_token
from aiogram import Bot, Dispatcher

from db import db

async def main():
    #Инициализация бота
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    #подключение базы
    db.init_db()

    #Подключение роутеров
    dp.include_router(start.router)
    dp.include_router(names_generate.router)
    dp.include_router(one_name.router)
    dp.include_router(edit_token.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())