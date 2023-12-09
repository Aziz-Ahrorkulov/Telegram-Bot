from aiogram import Bot, Dispatcher, types,executor
from aiogram.types.web_app_info import WebAppInfo
import asyncio

bot = Bot('6522840153:AAFr0EbaPSFh5cYoz7cvxBCknBC_oUS-h_w')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Добро пожаловать на наш бот! Мы рады вас видеть 🤍')
    await asyncio.sleep(0.5)
    await gender(message)

async def gender(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True, one_time_keyboard=True)
    gender_btn1 = types.KeyboardButton('Мальчик')
    gender_btn2 = types.KeyboardButton('Девочка')
    markup.add(gender_btn1, gender_btn2)
    await message.answer('Выберите пол', reply_markup=markup)

@dp.message_handler(lambda message: message.text in ['Мальчик', 'Девочка'])
async def callback_gender(message: types.Message):
    if message.text == 'Мальчик':
        await message.answer('Мужской пол', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer('Женский  пол', reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(0.5)
    await ask_name(message)

async def ask_name(message: types.Message):
    await message.answer('Введите свое имя 🖋!')

# Обработчик сообщений с именем пользователя
@dp.message_handler()
async def get_name(message: types.Message):
    user_name = message.text
    await message.answer(f'Красивое имя {user_name}!')
    await asyncio.sleep(0.5)
    await ask_age(message)

# Функция для запроса возраста пользователя
async def ask_age(message: types.Message):
    await message.answer('Введите ваш возраст:')

# Обработчик сообщений с возрастом пользователя
@dp.message_handler()
async def get_age(message: types.Message):
    # Проверяем, является ли введенное значение числом
    if message.text.isdigit():
        await photo_user(message)
        
    else:
        await message.answer('Пожалуйста, введите число в качестве возраста.')
     

async def photo_user(message: types.Message):
    pass

executor.start_polling(dp)