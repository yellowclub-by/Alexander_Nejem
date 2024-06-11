import asyncio
from aiogram import types
from aiogram import Bot, Dispatcher



TOKEN = '6558387187:AAFoSJPpEna_rrS8pJk9fjI1Juh5uHGBOJ0'
# связываем код с ботом в телеграме
bot = Bot(token=TOKEN)

# создаем диспетчер для обработки команд
dp = Dispatcher()


from handlers.user_privat import user_router
from handlers.user_group import group_router
from handlers.menu import menu_router
dp.include_router(user_router)
dp.include_router(menu_router)
dp.include_router(group_router)

# функция для старта бота
async def main():
    print('Bot is activate')
    await dp.start_polling(bot)


asyncio.run(main())
