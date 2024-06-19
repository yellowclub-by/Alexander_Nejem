from aiogram import Router, types, F
from aiogram.types import FSInputFile

menu_router = Router()

@menu_router.message(F.text.lower() == 'овсянныя печенья')
async def menu_cookis(message: types.Message):
    photo = FSInputFile('img\menu\печенькаs.jpeg')
    await message.answer_photo(photo, caption=f'это мое творение по имени "печенька"')

@menu_router.message(F.text.lower() == 'терамису')
async def menu_teramicy(message: types.Message):
    photo = FSInputFile('img\menu\терамису.jpeg')
    await message.answer_photo(photo, caption=f'это мое творение по имени "терамису"')

@menu_router.message(F.text.lower() == 'пироги')
async def menu_cake(message: types.Message):
    photo = FSInputFile('img\menu\пироги.jpeg')
    await message.answer_photo(photo, caption=f'это мое творение по имени "пироги"')

@menu_router.message(F.text.lower() == 'макароны')
async def menu_makaroni(message: types.Message):
    photo = FSInputFile('img\menu\макароны.jpeg')
    await message.answer_photo(photo, caption=f'это мое творение по имение "макароны"')
