import asyncio

from routers import start, group_create
from aiogram import Bot, Dispatcher

from db import db

import config

async def main():
    #Инициализация бота
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    #подключение базы
    db.init_db()

    #Подключение роутеров
    dp.include_router(start.router)
    dp.include_router(group_create.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())