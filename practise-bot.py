from aiogram import Bot, Dispatcher, types,executor
from aiogram.types.web_app_info import WebAppInfo
import asyncio
import marksup as nav
from database import Database



bot = Bot('6522840153:AAFr0EbaPSFh5cYoz7cvxBCknBC_oUS-h_w')
dp = Dispatcher(bot)


handler = Database('database.db')

# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     user_id = message.from_user.id
#     if not handler.user_exist(user_id):
#         handler.add_user(user_id)
#         await message.answer('Вы зарегистрированы!')
#     else:
#         nickname = handler.get_nickname(user_id)
#         await message.answer(f'Ваш никнейм: {nickname}')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if not handler.user_exist(user_id):
        handler.add_user(message.from_user.id)
        await message.answer('Укажите ваш ник')
    else:
        await message.answer('Вы уже зарегистрированы!', reply_markup=nav.mainmenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'ПРОФИЛЬ 🤵':
            user_nickname = "Ваш ник " + handler.get_user_info(message.from_user.id)
            await message.answer(user_nickname)
        elif message.text == 'НАСТРОЙКА 🛠':
            await message.answer('Выберите вариант что вы хотите изменить !', reply_markup=nav.changeMenu)
        else:
            if handler.get_signup(message.from_user.id) == 'setnickname':
                if len(message.text) > 20:  # Исправление здесь: исправлено синтаксическое условие проверки длины
                    await message.answer('Никнейм не должен превышать 20 символов')
                elif '@' in message.text or '/' in message.text:  # Исправление здесь: проверка наличия запрещенных символов
                    await message.answer('Вы ввели запрещенный символ')
                else:
                    if handler.set_nickname(message.from_user.id, message.text):
                        await asyncio.sleep(0.5)
                        await ask_age(message)
                    else:
                        await message.answer('Ошибка при установке никнейма. Попробуйте еще раз.')
            else:
                await message.answer('Что?')

@dp.message_handler()
async def ask_age(message: types.Message):
    message.answer('Ведите свой возраст : ')

# @dp.message_handler()
# async def bot_message(message: types.Message):
#     if message.chat.type == 'private':
#         if message.text == 'ПРОФИЛЬ 🤵':
#             user_nickname = "Ваш ник " + handler.get_name(message.from_user.id)
#             await message.answer(user_nickname)
#         else:
#             if handler.get_signup(message.from_user.id) == 'setnickname':
#                 if len(message.text) > 20:  
#                     await message.answer('Никнейм не должен превышать 20 символов')
#                 elif '@' in message.text or '/' in message.text:  
#                     await message.answer('Вы ввели запрещенный символ')
#                 else:
#                     if handler.set_nickname(message.from_user.id, message.text):
#                         handler.set_signup(message.from_user.id, "setage")  # Устанавливаем статус на установку возраста
#                         await message.answer('Пожалуйста, укажите свой возраст')
#                     else:
#                         await message.answer('Ошибка при установке никнейма. Попробуйте еще раз.')
#             elif handler.get_signup(message.from_user.id) == 'setage':  # Добавляем обработку установки возраста
#                 try:
#                     age = int(message.text)
#                     # Проверка на корректность возраста (можно добавить дополнительные условия)
#                     if age < 10 or age > 100:
#                         await message.answer('Пожалуйста, укажите реальный возраст')
#                     else:
#                         handler.set_age(message.from_user.id, age)  # Устанавливаем возраст
#                         handler.set_signup(message.from_user.id, "done")
#                         await message.answer('Регистрация прошла успешно', reply_markup=nav.mainmenu)
#                 except ValueError:
#                     await message.answer('Пожалуйста, введите число в качестве возраста')
#             else:
#                 await message.answer('Что?')
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.answer('Добро пожаловать на наш бот! Мы рады вас видеть 🤍')
#     await asyncio.sleep(0.5)
#     await gender(message)

# async def gender(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True, one_time_keyboard=True)
#     gender_btn1 = types.KeyboardButton('Мальчик')
#     gender_btn2 = types.KeyboardButton('Девочка')
#     markup.add(gender_btn1, gender_btn2)
#     await message.answer('Выберите пол', reply_markup=markup)

# @dp.message_handler(lambda message: message.text in ['Мальчик', 'Девочка'])
# async def callback_gender(message: types.Message):
#     if message.text == 'Мальчик':
#         await message.answer('Мужской пол', reply_markup=types.ReplyKeyboardRemove())
#     else:
#         await message.answer('Женский  пол', reply_markup=types.ReplyKeyboardRemove())
#     await asyncio.sleep(0.5)
#     await ask_name(message)

# async def ask_name(message: types.Message):
#     await message.answer('Введите свое имя 🖋!')

# # Обработчик сообщений с именем пользователя
# @dp.message_handler()
# async def get_name(message: types.Message):
#     user_name = message.text
#     await message.answer(f'Красивое имя {user_name}!')
#     await asyncio.sleep(0.5)
#     await ask_age(message)

# # Функция для запроса возраста пользователя
# async def ask_age(message: types.Message):
#     await message.answer('Введите ваш возраст:')

# # Обработчик сообщений с возрастом пользователя
# @dp.message_handler()
# async def get_age(message: types.Message):
#     # Проверяем, является ли введенное значение числом
#     if message.text.isdigit():
#         await photo_user(message)
        
#     else:
#         await message.answer('Пожалуйста, введите число в качестве возраста.')
     

# async def photo_user(message: types.Message):
#     pass
executor.start_polling(dp)