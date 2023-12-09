import re
from aiogram import Bot, Dispatcher, types, executor
import wikipedia

# Создаем экземпляр бота

bot = Bot('6522840153:AAFr0EbaPSFh5cYoz7cvxBCknBC_oUS-h_w')
dp = Dispatcher(bot)

# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")

# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всё после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

# Функция, обрабатывающая команду /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer('Отправьте мне любое слово, и я найду его значение на Wikipedia')

# Получение сообщений от юзера
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: types.Message):
    await message.answer(getwiki(message.text))
    await message.answer('Отправьте мне любое слово, заново !')

executor.start_polling(dp)