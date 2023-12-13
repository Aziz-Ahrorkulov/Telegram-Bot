from aiogram import types

btnback = types.KeyboardButton('Назад 👈🏻')

btnProfile = types.KeyboardButton('ПРОФИЛЬ 🤵')
btnSettings = types.KeyboardButton('НАСТРОЙКА 🛠')


mainmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
mainmenu.add(btnProfile, btnSettings)


btnChangeName = types.KeyboardButton('Изменит ник 🖊')
btnChangeAge = types.KeyboardButton('Изменит возраст 🔞')

changeMenu = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,  one_time_keyboard=True)
changeMenu.add(btnChangeName, btnChangeAge, btnback)