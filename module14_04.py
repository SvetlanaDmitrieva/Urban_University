# Дополните ранее написанный код для Telegram-бота:
# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - тест
# price(цена) - целое число (не пустой)
# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
#
# Изменения в Telegram-бот:
# В самом начале запускайте ранее написанную функцию get_all_products.
# Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации
# продуктов функцию get_all_products. Полученные записи используйте в выводимой надписи:
# "Название: <title> | Описание: <description> | Цена: <price>"

import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.input_file import InputFile

import crud_functions as cf
import asyncio

api = "_____________________________"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text='Рассчитать')
btn2 = KeyboardButton(text='Информация')
btn3 = KeyboardButton(text='Купить')
kb1.add(btn1, btn2)
kb1.add(btn3)

kb_in = InlineKeyboardMarkup(resize_keyboard=True)
btn_in_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
btn_in_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.add(btn_in_1, btn_in_2)

kb_in_2 = InlineKeyboardMarkup(resize_keyboard=True)
btn_in_p1 = InlineKeyboardButton(text='Продукт1', callback_data='product_buying')
btn_in_p2 = InlineKeyboardButton(text='Продукт2', callback_data='product_buying')
btn_in_p3 = InlineKeyboardButton(text='Продукт3', callback_data='product_buying')
btn_in_p4 = InlineKeyboardButton(text='Продукт4', callback_data='product_buying')
kb_in_2.row(btn_in_p1, btn_in_p2, btn_in_p3, btn_in_p4)

list_photo = ['foto/betonomeshalka-01.png', 'foto/excavator.png', 'foto/katok.png', 'foto/musorovoz-01.png']
products = cf.get_all_products()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.', reply_markup=kb1)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message: types.Message):
    for product in products:
        await message.answer(f'Название:{product[1]}/Описание:{product[2]}/Цена:{product[3]}')
        await bot.send_photo(chat_id=message.from_user.id, photo=InputFile(list_photo[int(f'{product[0]}')-1]))
    await  message.answer('Выберите продукт для покупки: ', reply_markup=kb_in_2)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await  call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    str1 = 'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;'
    str2 = 'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.'
    await call.message.answer(f"{str1} \n {str2}")
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    for_man = (10 * float(data['weight']) + 6.25 * float(data['growth']) -
               5 * float(data['age']) - 5)
    for_woman = for_man - 166
    await message.answer(f'Норма калорий для мужчин: {for_man}, для женщин: {for_woman}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
