from aiogram import Bot, Dispatcher, types, executor
import marksup as nav
from database import Database

bot = Bot('6522840153:AAFr0EbaPSFh5cYoz7cvxBCknBC_oUS-h_w')
dp = Dispatcher(bot)
handler = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if not handler.user_exist(user_id):
        handler.add_user(user_id)
        await message.answer('Укажите ваш ник')
    else:
        await message.answer('Вы уже зарегистрированы!', reply_markup=nav.mainmenu)

@dp.message_handler(commands=['profile'])
async def show_profile(message: types.Message):
    user_info = "Ваш профиль: \n \n" + handler.get_user_info(message.from_user.id)
    await message.answer(user_info)

@dp.message_handler(commands=['settings'])
async def show_settings(message: types.Message):
    await message.answer('Выберите вариант, который вы хотите изменить!', reply_markup=nav.changeMenu)

@dp.message_handler(lambda message: message.text in ['Изменит анкету 🖊', 'Назад 👈🏻'])
async def change_settings(message: types.Message):
    if message.text == 'Изменит анкету 🖊':
        await change_account_settings(message)
    elif message.text == 'Назад 👈🏻':
        await start(message)  

@dp.message_handler(lambda message: message.text == 'Изменит анкету 🖊')
async def change_account_settings(message: types.Message):
    user_id = message.from_user.id
    if handler.user_exist(user_id):
        last_nickname = handler.get_last_nickname(user_id)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton(last_nickname))
        await message.answer('Введите новый никнейм или нажмите на предыдущий никнейм для использования его:', reply_markup=keyboard)
        handler.set_signup(user_id, "setnickname")
    else:
        await start(message)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'ПРОФИЛЬ 🤵':
            await show_profile(message)
        elif message.text == 'НАСТРОЙКА 🛠':
            await show_settings(message)
        else:
            if handler.get_signup(message.from_user.id) == 'setnickname':
                if len(message.text) > 20 or '@' in message.text or '/' in message.text:
                    await message.answer('Некорректный никнейм')
                else:
                    if handler.set_nickname(message.from_user.id, message.text):
                        await message.reply(f'Красивое имя {message.text}')
                        handler.set_signup(message.from_user.id, "setage")
                        await ask_age(message)
                    else:
                        await message.answer('Ошибка при установке никнейма. Попробуйте еще раз.')
            else:
                await process_age(message)

async def ask_age(message: types.Message):
    user_id = message.from_user.id
    last_age = handler.get_last_age(user_id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(str(last_age)))
    await message.answer('Введите ваш возраст или нажмите на предыдущий возраст для использования его:', reply_markup=keyboard)

@dp.message_handler()
async def process_age(message: types.Message):
    if handler.get_signup(message.from_user.id) == 'setage':
        if len(message.text) > 20 or not message.text.isdigit() or int(message.text) < 10:
            await message.answer('Некорректный возраст')
        else:
            if handler.set_age(message.from_user.id, message.text):
                handler.set_signup(message.from_user.id, "setgender")
                await ask_gender(message)
            else:
                await message.answer('Ошибка при сохранении возраста. Попробуйте еще раз.')
    else:
        await process_gender(message)

async def ask_gender(message: types.Message):
    await message.answer('Выберите пол: ', reply_markup=nav.genderMenu)

@dp.message_handler()
async def process_gender(message: types.Message):
    if handler.get_signup(message.from_user.id) == 'setgender':
        user_id = message.from_user.id
        if message.text.lower() not in ['male', 'female'] and message.text not in ['Male 🚹', 'Female 🚺']:
            await message.answer('Выберите пол из списка')
        else:
            if handler.set_gender(user_id, message.text):
                handler.set_signup(user_id, "done")
                await message.answer('Регистрация прошла успешно ! ❤', reply_markup=nav.mainmenu)
            else:
                await message.answer('Ошибка при сохранении пола. Попробуйте еще раз.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
