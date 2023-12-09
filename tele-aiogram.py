from aiogram import Bot, Dispatcher, types,executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6522840153:AAFr0EbaPSFh5cYoz7cvxBCknBC_oUS-h_w')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='yes'))
    await message.answer(f'Привет {message.from_user.first_name} { message.from_user.last_name } добро пожаловать на наш бот ! \nХотите познакомиться с нашой фермой', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    if call.data == 'yes':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти на наш сайт', url='https://youtube.com'))
        await call.message.answer('Наша ферма очень полезная для вас !', reply_markup=markup)


# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     markup.add(types.KeyboardButton('Site', web_app=WebAppInfo(url='https://youtube.com')))
    # markup.add(types.KeyboardButton('Instagram', callback='instagram'))
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Web', url='https://jizzaxyt.uz'))
    # markup.add(types.InlineKeyboardButton('Go', callback_data='go'))

    # await message.answer('Привет', reply_markup=markup)


# @dp.callback_query_handler()
# async def callback(call):
#     await call.message.answer(call.data)



# @dp.message_handler()
# async def website(message: types.Message):
#     markup = types.ReplyKeyboardMarkup()
#     markup.add(types.KeyboardButton('Site', url='site'))
#     markup.add(types.KeyboardButton('Instagram', callback='instagram'))
#     await message.answer('Web', reply_markup=markup)



# @dp.callback_query_handler()
# async def site(call):
#     await call.message.url(call, 'https://jizzaxyt.uz/')






executor.start_polling(dp)