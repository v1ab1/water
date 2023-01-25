import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton

from excel_handler import excel_handle

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


update = False

# buttonAnalisys = InlineKeyboardButton("Показать актуальный анализ", callback_data="show_analysis")
# buttonUpdate = InlineKeyboardButton("Вкл. автообновление", callback_data="enable_auto_update")
# buttonDiscounts = InlineKeyboardButton("Показать скидки", callback_data="show_discounts")
# keyboard = InlineKeyboardMarkup().add(buttonAnalisys, buttonUpdate, buttonDiscounts)

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


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот, который покажет тебя самую актуальную информацию о рынке воды в Челябинске! \nХочешь получить сводку?")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Выберите вариант!", reply_markup=keyboard)
    # await message.answer('Сейчас подготовим для тебя актуальный анализ рынка!')
    # await message.answer('Подождите...')
    # await excel_handle()
    # await bot.send_document(message.from_user.id, open('analysis.xlsx', 'rb'))
    # await message.answer('Готово! :)')


# async def excel_update():
#     if update:
#         await excel_handle()


# job = Dispatcher.job(excel_update, interval=86400)
# scheduler = Dispatcher.scheduler()
# scheduler.add_job(job)
# scheduler.start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

