from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton

kbFalse = [
    [
        InlineKeyboardButton("Актуальный анализ", callback_data="analysis"),
    ],
    [
        InlineKeyboardButton("Акции", callback_data="discounts"),
    ],
    [
        InlineKeyboardButton('Вкл. автообновление✅', callback_data="auto_update")
    ],
    [
        InlineKeyboardButton('Заменить Excel', callback_data="excel")
    ]
]

keyboardFalse = InlineKeyboardMarkup(inline_keyboard=kbFalse)

kbTrue = [
    [
        InlineKeyboardButton("Актуальный анализ", callback_data="analysis"),
    ],
    [
        InlineKeyboardButton("Акции", callback_data="discounts"),
    ],
    [
        InlineKeyboardButton('Выкл. автообновление🚫', callback_data="auto_update")
    ],
    [
        InlineKeyboardButton('Заменить Excel', callback_data="excel")
    ]
]

keyboardTrue = InlineKeyboardMarkup(inline_keyboard=kbTrue)

yes = [
    [
        InlineKeyboardButton("Да", callback_data="yes"),
    ],
]

yes_button = InlineKeyboardMarkup(inline_keyboard=yes)

sumbit = [
    [
        InlineKeyboardButton("Да", callback_data="submit"),
    ],
    [
        InlineKeyboardButton("Нет", callback_data="cancel"),
    ]
]

sumbit_buttons = InlineKeyboardMarkup(inline_keyboard=sumbit)

choose_type = [
    [
        InlineKeyboardButton("PDF", callback_data="pdf"),
    ],
    [
        InlineKeyboardButton("Картинками", callback_data="pictures"),
    ],
    [
        InlineKeyboardButton("Вернуться в меню", callback_data="menu"),
    ]
]

choose_type_keyboard = InlineKeyboardMarkup(inline_keyboard=choose_type)