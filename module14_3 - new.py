# Подготовьте Telegram-бота из последнего домашнего задания 13 моудля сохранив код с ним
# в файл module_14_3.py.
# Дополните ранее написанный код для Telegram-бота:
# Создайте и дополните клавиатуры:
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"
# Создайте хэндлеры и функции к ним:
# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
# Функция get_buying_list должна выводить надписи 'Название: Product<number> |
# Описание: описание <number> | Цена: <number * 100>' 4 раза. После каждой надписи выводите
# картинки к продуктам. В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.input_file import InputFile

import foto as ft
from PIL import Image

import asyncio

api = "______________________________"
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
captions = [
    'Название:Product 1 | Описание:описание 1 | Цена:100',
    'Название:Product 2 | Описание:описание 2 | Цена:200',
    'Название:Product 3 | Описание:описание 3 | Цена:300',
    'Название:Product 4 | Описание:описание 4 | Цена:400'
]


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
    for i in range(4):
        await message.answer(f'{captions[i]}')
        await bot.send_photo(chat_id=message.from_user.id, photo=InputFile(list_photo[i]))
    await  message.answer('Выберите продукт для покупки: ', reply_markup=kb_in_2)


@dp.callback_query_handler(text= ['product_buying'])
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
