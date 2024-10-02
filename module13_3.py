# К коду из подготовительного видео напишите две асинхронные функции:
# start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' . Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий декоратор)
# all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'. Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)
# Запустите ваш Telegram-бот и проверьте его на работоспособность.
# Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
# Запустите ваш Telegram-бот и проверьте его на работоспособность.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "_______________________"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
