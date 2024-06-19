from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keybords import reply, inline

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"<b>Привет</b>, это бот кафe 'Tiks'", reply_markup=reply.start_kb )


@user_router.message(F.text.lower() == 'меню')
@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer(f"Это наша меню в кафе:", reply_markup=reply.menu_kb)


@user_router.message(F.text.lower() == 'про нас')
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer(
        f"О нас: Tiks, это кафе,где продают вкусные иж недорогие десерты и мы уверены, что вы найдете то что хотите",
    reply_markup=inline.links_kb)


@user_router.message(F.text.lower() == 'адреса')
@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Адреса", reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_types(callback: types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == '1':
        await callback.message.answer('Ул. Уютная 2')
    elif query == '2':
        await callback.message.answer('Пр. Независимости 52')
    else:
        await callback.message.answer('Ул. Шкловская 4')
    await callback.answer()


@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(message: types.Message):
    await message.answer("Контакт: 80445118158")


@user_router.message(F.text.lower() == 'назад')
async def back(message: types.Message):
    await message.answer('Главное меню',  reply_markup=reply.start_kb)


# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.sticker)
# @user_router.message(F.text.lower() == 'доставка')
# @user_router.message(F.text.lower().contains('доставк'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith("как"), F.text.lower().endswith('?'))
# @user_router.message( (F.text.lower().contains('стоимост') ) | (F.text.lower().contains('цен')) )



async def echo(message: types.Message):
    await message.answer("Сработал 'Магический фильтр'")