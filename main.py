import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton

from excel_handler import excel_handle

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

update = False

kb = [
    [
        InlineKeyboardButton("Актуальный анализ", callback_data="analysis"),
    ],
    [
        InlineKeyboardButton("Акции", callback_data="discounts"),
    ],
    [
        InlineKeyboardButton("Вкл. автообновление✅", callback_data="auto_update")
    ]
]

keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

yes = [
    [
        InlineKeyboardButton("Да", callback_data="yes"),
    ],
]

yes_button = InlineKeyboardMarkup(inline_keyboard=yes)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот, который покажет тебя самую актуальную информацию о рынке воды в Челябинске! \nХочешь получить сводку?", reply_markup=yes_button)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Выберите вариант!", reply_markup=keyboard)

@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'analysis':
        await bot.send_message(callback_query.from_user.id, 'Сейчас подготовим для тебя актуальный анализ рынка!')
        await bot.send_message(callback_query.from_user.id, 'Подождите...')
        await excel_handle()
        await bot.send_document(callback_query.from_user.id, open('analysis.xlsx', 'rb'))
        await bot.send_message(callback_query.from_user.id, 'Готово! :)')
        pass
    elif callback_query.data == 'discounts':
        # Ваш код для выполнения функции discounts()
        pass
    elif callback_query.data == 'auto_update':
        # Ваш код для выполнения функции auto_update()
        pass
    elif callback_query.data == 'yes':
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboard)
        pass

# async def excel_update():
#     if update:
#         await excel_handle()


# job = Dispatcher.job(excel_update, interval=86400)
# scheduler = Dispatcher.scheduler()
# scheduler.add_job(job)
# scheduler.start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

