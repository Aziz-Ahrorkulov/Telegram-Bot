from aiogram import types

btnback = types.KeyboardButton('Назад 👈🏻')

btnProfile = types.KeyboardButton('ПРОФИЛЬ 🤵')
btnSettings = types.KeyboardButton('НАСТРОЙКА 🛠')
btnOUT = types.KeyboardButton('УДАЛИТЬ АККАУНТ ❌')


btnGenderMale = types.KeyboardButton('Male 🚹')
btnGenderFemale = types.KeyboardButton('Female 🚺')



genderMenu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,  one_time_keyboard=True)
genderMenu.add(btnGenderMale, btnGenderFemale)




mainmenu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
mainmenu.add(btnProfile, btnSettings, btnOUT)


btnChangeName = types.KeyboardButton('Изменит анкету 🖊')

changeMenu = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,  one_time_keyboard=True)
changeMenu.add(btnChangeName, btnback)