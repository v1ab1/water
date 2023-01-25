import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton
import schedule
import time

from excel_handler import excel_handle
from discounts_handler import discounts_handle
from discounts_sender import discounts_send

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

my_file = open("update.txt", "r")
update = my_file.read()
my_file.close()

async def check_update(change):
    my_file = open("update.txt", "r")
    update = my_file.read()
    my_file.close()
    if change:
        update = "True" if update == "False" else "False"
        my_file = open("update.txt", "w")
        my_file.write(f'{update}')
        my_file.close()
    return update

kbFalse = [
    [
        InlineKeyboardButton("Актуальный анализ", callback_data="analysis"),
    ],
    [
        InlineKeyboardButton("Акции", callback_data="discounts"),
    ],
    [
        InlineKeyboardButton('Вкл. автообновление✅', callback_data="auto_update")
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
    ]
]

keyboardTrue = InlineKeyboardMarkup(inline_keyboard=kbTrue)

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
    update = await check_update(False)
    await message.answer("Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)

@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'analysis':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Сейчас подготовим для тебя актуальный анализ рынка!')
        await bot.send_message(callback_query.from_user.id, 'Подождите...')
        await excel_handle()
        await bot.send_document(callback_query.from_user.id, open('analysis.xlsx', 'rb'))
        await bot.send_message(callback_query.from_user.id, 'Готово! :)')
        update = await check_update(False)
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'discounts':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Сейчас покажу тебе актуальные скидки!')
        await bot.send_message(callback_query.from_user.id, 'Подождите...')
        await discounts_handle()
        await discounts_send(bot, callback_query)
        await bot.send_message(callback_query.from_user.id, 'Готово!...')
        update = await check_update(False)
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'auto_update':
        await callback_query.message.delete()
        update = await check_update(False)
        if update == "True":
            await bot.send_message(callback_query.from_user.id, "Автообновление включено!")
        else:
            await bot.send_message(callback_query.from_user.id, "Автообновление выключено!")
        update = await check_update(True)
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'yes':
        await callback_query.message.delete()
        update = await check_update(False)
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass

def job():
    update = check_update(False)
    if (update == "True"):
        excel_handle()

schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

