from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, это бот фастфуд")


@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer(f"Это наша меню в фастфуде:")


@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer(
        f"О нас: Tiks, это фастфуд,где продают вкусную иж недорогую еду и заказ будут везти"
        f"от 20 минут")


@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Адреса:")


@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("Контакт: 80445118158")


@user_router.message()
async def echo(message: types.Message):
    await message.answer("бот находться в разработке")
    user_text = message.text
    await message.answer(user_text)
