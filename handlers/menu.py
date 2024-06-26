from aiogram import Router, types, F
from aiogram.types import FSInputFile

menu_router = Router()

@menu_router.message(F.text.lower() == 'овсянныя печенья')
async def menu_cookis(message: types.Message):
    photo = FSInputFile('img\menu\печенькаs.jpeg')
    await message.answer_photo(photo, caption=f'''Овсянная печенья
    
овсянная печенья с привкусом банана

стоимость товара: 6 шт. 6.59 рублей или 12 шт. 10.59 рублей''')

@menu_router.message(F.text.lower() == 'терамису')
async def menu_teramicy(message: types.Message):
    photo = FSInputFile('img\menu\терамису.jpeg')
    await message.answer_photo(photo, caption=f'''Терамису

Маленький вкусный десерт, который стоит пробовать в холодном составе с кофе

стоимость товара: 1 шт. 5.99 рублей или 3 шт. 16.99 рублей''')

@menu_router.message(F.text.lower() == 'пироги')
async def menu_cake(message: types.Message):
    photo = FSInputFile('img\menu\пироги.jpeg')
    await message.answer_photo(photo, caption=f'''Пироги 

В наших пирогах имеется 3 вкуса: клубничный, яблочный и ягодный

стоимость товара: клубничный 20.99 рублей, яблочный 15.99 рублей, ягодный 25.99 рублей''')

@menu_router.message(F.text.lower() == 'макароны')
async def menu_makaroni(message: types.Message):
    photo = FSInputFile('img\menu\макароны.jpeg')
    await message.answer_photo(photo, caption=f'''Макароны 

Макароны, вкусные маленькие сладости которые имеют разнообразные цвета(синий, голубой, розовый, желтый и тд.

стоимость товара:  6 шт. 9.99 рублей или 12 шт. 18.99 рублей''')
