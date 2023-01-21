import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile


API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот, который покажет тебя самую актуальную информацию о рынке воды в Челябинске! \nХочешь получить актуальную сводку?")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Сейчас подготовим для тебя актуальный анализ рынка!')
    await message.answer('Подождите...')
    await bot.send_document(message.from_user.id, open('analysis.xlsx', 'rb'))
    await message.answer('Готово! :)')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

