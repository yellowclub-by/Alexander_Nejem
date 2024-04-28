import asyncio
from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart


TOKEN = '6558387187:AAFoSJPpEna_rrS8pJk9fjI1Juh5uHGBOJ0'
# связываем код с ботом в телеграме
bot = Bot(token=TOKEN)

# создаем диспетчер для обработки команд
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, это бот фастфуд")


@dp.message()
async def echo(message: types.Message):
    await message.answer("бот находться в разработке")
    user_text = message.text
    await message.answer(user_text)


# функция для старта бота
async def main():
    await dp.start_polling(bot)


asyncio.run(main())
