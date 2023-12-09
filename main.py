import telebot
import json
from telebot import types

bot = telebot.TeleBot('6522840153:AAFr0EbaPSFh5cYoz7cvxBCknBC_oUS-h_w')
 












# < -- Курс Валют -- >
# from currency_converter import CurrencyConverter 
# currency = CurrencyConverter()
# amount = 0

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет рад вас видеть! Ведите сумму: ')
#     bot.register_next_step_handler(message, summa)


# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный формат! Впишите сумму')
#         bot.register_next_step_handler(message, summa)
#         return 
#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn3 = types.InlineKeyboardButton('USD/UZS', callback_data='usd/uzs')
#         btn4 = types.InlineKeyboardButton('Другое', callback_data='else')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Число должно быть больше за 0. Впишите сумму')
#         bot.register_next_step_handler(message, summa)


# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data != 'else':
#         values = call.data.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Получаеться: {round(res, 2) }. Можете ввести другую сумму !')
#         bot.register_next_step_handler(call.message, summa)

#     else:
#         bot.send_message(call.message.chat.id, 'Ведите пару значение через слеш !')
#         bot.register_next_step_handler(call.message, my_currency)

# def my_currency(message):
#     try:
#         values = message.text.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Получаеться: {round(res, 2) }. Можете ввести другую сумму !')
#         bot.register_next_step_handler(message, summa)
#     except Exception:
#         bot.send_message(message.chat.id, 'Что-то не так. Впишите значение заново')
#         bot.register_next_step_handler(message, my_currency)    



# < -- Create the weather info bot -- >

# import requests

# API = '518b70f462479acf021f439ea598559c'

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет Рад тебя видеть! Напиши название города: ')

# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     if res.status_code == 200:
#         data = json.loads(res.text)
#         temp = data["main"]["temp"]
#         bot.reply_to(message, f'Сейчас погода: {temp}')

#         img = 'sunny.jpg' if temp > 5.0 else 'sun-cloud.jpg'
#         file = open('./' + img, 'rb')
#         bot.send_photo(message.chat.id, file)

#     else:
#         bot.reply_to(message, 'Город указан не верно')

# < -- Create the Database for user -->


# import psycopg2
# import sqlite3

# name = None


# @bot.message_handler(commands=['start'])
# def main(message):

#     conn = sqlite3.connect('telegram.sql')
#     cur = conn.cursor()

#     cur.execute('CREATE TABLE IF NOT EXISTS user(id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()

#     bot.send_message(message.chat.id, f'Привет! Напишите свое имя: ')
#     bot.register_next_step_handler(message, user_name)

# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, f'Напишите свой пароль: ')
#     bot.register_next_step_handler(message, user_pass)  

# def user_pass(message):
#     password = message.text.strip()
    
#     conn = sqlite3.connect('telegram.sql')
#     cur = conn.cursor()

#     cur.execute("INSERT INTO user(name, pass) VALUES ('%s', '%s')" % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()


#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='user_list'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)

# @bot.callback_query_handler(func=lambda call:True)
# def callback(call):

#     conn = sqlite3.connect('telegram.sql')
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM user")
#     users = cur.fetchall()

#     info = ''

#     for el in users:
#         info += f'Имя {el[1]}, пароль {el[2]}\n'

#     cur.close()
#     conn.close()

#     bot.send_message(call.message.chat.id, info)

# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

bot.polling(none_stop=True)