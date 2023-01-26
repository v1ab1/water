import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton
import schedule
import time
import os

from excel_handler import excel_handle
from graph_handler import graph_handle
from discounts_handler import discounts_handle
from discounts_sender import discounts_send
from pdf_maker import pdf_make

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

sumbit_button = InlineKeyboardMarkup(inline_keyboard=sumbit)

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


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот, который покажет тебя самую актуальную информацию о рынке воды в Челябинске! \nХочешь получить сводку?", reply_markup=yes_button)


@dp.message_handler()
async def echo(message: types.Message):
    update = await check_update(False)
    await message.answer("Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)

@dp.message_handler(content_types=['document'])
async def process_document(message: types.Message):
    doc = message.document
    await doc.download(destination_file='./temp_analysis.xlsx')
    await message.answer("Вы действительно хотите заменить Excel файл на сервере?", reply_markup=sumbit_button)

@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):
    update = await check_update(False)
    if callback_query.data == 'analysis':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Сейчас подготовим для тебя актуальный анализ рынка!')
        await bot.send_message(callback_query.from_user.id, 'Подождите...')
        await excel_handle()
        await graph_handle()
        await bot.send_document(callback_query.from_user.id, open('analysis.xlsx', 'rb'))
        await bot.send_message(callback_query.from_user.id, 'Готово! :)')
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'discounts':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, "В каком формате хочешь получить скидки?", reply_markup=choose_type_keyboard)
        pass
    elif callback_query.data == 'pictures':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Сейчас покажу тебе актуальные скидки!')
        await bot.send_message(callback_query.from_user.id, 'Подождите...')
        await discounts_handle()
        await discounts_send(bot, callback_query)
        await bot.send_message(callback_query.from_user.id, 'Готово!...')
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'pdf':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Сейчас покажу тебе актуальные скидки!')
        await bot.send_message(callback_query.from_user.id, 'Подождите...')
        await discounts_handle()
        await pdf_make()
        await bot.send_document(callback_query.from_user.id, open('discounts.pdf', 'rb'))
        await bot.send_message(callback_query.from_user.id, 'Готово!...')
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'auto_update':
        await callback_query.message.delete()
        if update == "True":
            await bot.send_message(callback_query.from_user.id, "Автообновление включено!")
        else:
            await bot.send_message(callback_query.from_user.id, "Автообновление выключено!")
        update = await check_update(True)
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'yes':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'excel':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, "Отправьте Excel файл для замены на сервере")
        await bot.send_message(callback_query.from_user.id, "Внимание!\nДля корректной работы необходимы следующие условия:\n1)Первая страница должна быть скопирована с предыдущего файла(необходимо такое же название и наличие таблицы в таким же форматированием)\n2)Наличие хотя бы одной страницы с датами и таким же форматированием как в предыдущем файле\n3)Файл должен называться 'analysis.xlsx'")
        pass
    elif callback_query.data == 'submit':
        await callback_query.message.delete()
        try:
            os.remove('old_analysis.xlsx')
        except:
            pass
        os.rename('analysis.xlsx', 'old_analysis.xlsx')
        os.rename('temp_analysis.xlsx', 'analysis.xlsx')
        await bot.send_message(callback_query.from_user.id, "Файл заменен")
        await bot.send_message(callback_query.from_user.id, "Готово!")
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'cancel':
        await callback_query.message.delete()
        os.remove('temp_analysis.xlsx')
        await bot.send_message(callback_query.from_user.id, "Действие отменено")
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'menu':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass

async def job():
    update = await check_update(False)
    if (update == "True"):
        await excel_handle()
        await graph_handle()

async def service():
    schedule.every().day.at("07:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    service()
    executor.start_polling(dp, skip_updates=True)