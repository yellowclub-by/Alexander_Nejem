from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='адрес 1', callback_data='addresses_1'),
        InlineKeyboardButton(text='адрес 2', callback_data='addresses_2'),
        InlineKeyboardButton(text='адрес 3', callback_data='addresses_3'),
        width=2
    )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сайт', url='https://pirogov.by/deserty/'),
            InlineKeyboardButton(text='Телеграмм', url='tg://resolve?domain=cantata_ru')
        ]
    ]
)
