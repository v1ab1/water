import logging
import time
import schedule
import os
import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from defs.keyboards import keyboardFalse, keyboardTrue, yes_button, sumbit_buttons, choose_type_keyboard
from defs.update_checker import update_check
from utils.excel_handler import excel_handle
from utils.graph_handler import graph_handle
from utils.prices_handler import prices_handle
from utils.discounts_handler import discounts_handle
from utils.discounts_sender import discounts_send
from utils.pdf_maker import pdf_make

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN.TOKEN)
dp = Dispatcher(bot)

update_check(False)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот, который покажет тебя самую актуальную информацию о рынке воды в Челябинске! \nХочешь получить сводку?", reply_markup=yes_button)


@dp.message_handler()
async def echo(message: types.Message):
    update = await update_check(False)
    await message.answer("Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)

@dp.message_handler(content_types=['document'])
async def process_document(message: types.Message):
    doc = message.document
    await doc.download(destination_file='./data/temp_analysis.xlsx')
    await message.answer("Вы действительно хотите заменить Excel файл на сервере?", reply_markup=sumbit_buttons)

@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):
    update = await update_check(False)
    if callback_query.data == 'analysis':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, 'Сейчас подготовим для тебя актуальный анализ рынка!')
        await bot.send_message(callback_query.from_user.id, 'Подождите...')
        await excel_handle()
        await graph_handle()
        await bot.send_document(callback_query.from_user.id, open('data/analysis.xlsx', 'rb'))
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
        await bot.send_document(callback_query.from_user.id, open('./data/discounts.pdf', 'rb'))
        await bot.send_message(callback_query.from_user.id, 'Готово!...')
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'auto_update':
        await callback_query.message.delete()
        update = await update_check(True)
        if update == "True":
            await bot.send_message(callback_query.from_user.id, "Автообновление включено!")
        else:
            await bot.send_message(callback_query.from_user.id, "Автообновление выключено!")
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
            os.remove('./data/old_analysis.xlsx')
        except:
            pass
        os.rename('./data/analysis.xlsx', './data/old_analysis.xlsx')
        os.rename('./data/temp_analysis.xlsx', './data/analysis.xlsx')
        await bot.send_message(callback_query.from_user.id, "Файл заменен")
        await bot.send_message(callback_query.from_user.id, "Готово!")
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'cancel':
        await callback_query.message.delete()
        os.remove('./data/temp_analysis.xlsx')
        await bot.send_message(callback_query.from_user.id, "Действие отменено")
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'menu':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass
    elif callback_query.data == 'prices':
        await callback_query.message.delete()
        await bot.send_message(callback_query.from_user.id, "Сейчас покажу цены!")
        await bot.send_message(callback_query.from_user.id, "Подождите...")
        await excel_handle()
        prices = await prices_handle()
        await bot.send_message(callback_query.from_user.id, f"Актуальные цены на воду за 2 тары:\n    Аква-мобиль Аква = {prices[0]}\n    Аква-мобиль Архыз = {prices[1]}\n    Аква-мобиль Артенза = {prices[2]}\n    Аква-мобиль Кукузар = {prices[3]}\n    Аква-мобиль Сосновская = {prices[4]}\n    Чебаркульский исток = {prices[5]}\n    Кристальная = {prices[6]}\n    Горный Оазис = {prices[7]}\n    Любимая = {prices[8]}\n    Люкс Вода = {prices[9]}\n    Люкс Вода Люксик = {prices[10]}\n    Ниагара = {prices[11]}\n    Ниагара Премиум = {prices[12]}\n    Ниагара Премиум Кавказ = {prices[13]}\n    Власов Ключ = {prices[14]}\n    Живая = {prices[15]}")
        await bot.send_message(callback_query.from_user.id, "Выберите вариант!", reply_markup=keyboardTrue if update == "True" else keyboardFalse)
        pass

async def job():
    update = await update_check(False)
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