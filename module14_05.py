# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
# initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL
# запроса. Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число (не пустой)
# balance - целое число (не пустой)
# add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
# Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
# Баланс у новых пользователей всегда равен 1000. Для добавления записей в таблице используйте SQL запрос.
# is_included(username) принимает имя пользователя и возвращает True, если такой пользователь
# есть в таблице Users, в противном случае False. Для получения записей используйте SQL запрос.
#
# Изменения в Telegram-бот:
# Кнопки главного меню дополните кнопкой "Регистрация".
# Напишите новый класс состояний RegistrationState с следующими объектами класса State: username,
# email, age, balance(по умолчанию 1000).
# Создайте цепочку изменений состояний RegistrationState.
# Фукнции цепочки состояний RegistrationState:
# sing_up(message):
# Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
# Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
# После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.
# set_username(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
# Функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
# Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username
# на message.text. Далее выводится сообщение "Введите свой email:" и принимается новое состояние
# RegistrationState.email.
# Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует,
# введите другое имя" и запрашивать новое состояние для RegistrationState.username.
# set_email(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
# Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
# Далее выводить сообщение "Введите свой возраст:":
# После ожидать ввода возраста в атрибут RegistrationState.age.
# set_age(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
# Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
# Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users при помощи
# ранее написанной crud-функции add_user.
# В конце завершать приём состояний при помощи метода finish().

import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.input_file import InputFile

import crud_functions_1 as cf
import asyncio

api = "8139360825:AAEZhFEErAQpAJj835vjBmmbq5jE1a8Yg70"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
btn0 = KeyboardButton(text='Регистрация')
btn1 = KeyboardButton(text='Рассчитать')
btn2 = KeyboardButton(text='Информация')
btn3 = KeyboardButton(text='Купить')
kb1.add(btn0)
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


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text=['Регистрация'])
async def sign_up(message):
    await message.answer("Введите имя пользователя(только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    user_included = cf.is_included(message.text)
    if user_included :
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()
        return
    await state.update_data(username=message.text)
    await message.answer("Введите свой email")
    await RegistrationState.email.set()


@dp.message_handler(state= RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email = message.text)
    await message.answer("Введите свой возраст")
    await RegistrationState.age.set()


@dp.message_handler(state= RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)
    data = await state.get_data()
    cf.add_user(data['username'],data['email'], data['age'] )
    await message.answer(f'Регистрация прошла успешно')
    await state.finish()


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
