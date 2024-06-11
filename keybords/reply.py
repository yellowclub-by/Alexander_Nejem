from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = KeyboardButton(text='Назад')

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='Про нас'),

        ],
        [
            KeyboardButton(text='Адреса'),
            KeyboardButton(text='Контакты')

        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Как я могу вам помочь?'

)

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Овсянныя печенья'),
        KeyboardButton(text='Терамису')
        ],
        [
        KeyboardButton(text='Пироги'),
        KeyboardButton(text='Макароны')
        ],
        [
            back_btn
        ]

    ],
    resize_keyboard=True
)
