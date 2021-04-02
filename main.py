import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup as BS

r1 = requests.get('http://gooroo.pp.ua/content/astrology/today/Aries.html')
r2 = requests.get('http://gooroo.pp.ua/content/astrology/today/Taurus.html')
r3 = requests.get('http://gooroo.pp.ua/content/astrology/today/Gemini.html')
r4 = requests.get('http://gooroo.pp.ua/content/astrology/today/Cancer.html')
r5 = requests.get('http://gooroo.pp.ua/content/astrology/today/Leo.html')
r6 = requests.get('http://gooroo.pp.ua/content/astrology/today/Virgo.html')
r7 = requests.get('http://gooroo.pp.ua/content/astrology/today/Libra.html')
r8 = requests.get('http://gooroo.pp.ua/content/astrology/today/Scorpio.html')
r9 = requests.get('http://gooroo.pp.ua/content/astrology/today/Sagittarius.html')
r10 = requests.get('http://gooroo.pp.ua/content/astrology/today/Capricorn.html')
r11 = requests.get('http://gooroo.pp.ua/content/astrology/today/Aquarius.html')
r12 = requests.get('http://gooroo.pp.ua/content/astrology/today/Pisces.html')
html1 = BS(r1.content, 'html.parser')
html2 = BS(r2.content, 'html.parser')
html3 = BS(r3.content, 'html.parser')
html4 = BS(r4.content, 'html.parser')
html5 = BS(r5.content, 'html.parser')
html6 = BS(r6.content, 'html.parser')
html7 = BS(r7.content, 'html.parser')
html8 = BS(r8.content, 'html.parser')
html9 = BS(r9.content, 'html.parser')
html10 = BS(r10.content, 'html.parser')
html11 = BS(r11.content, 'html.parser')
html12 = BS(r12.content, 'html.parser')
bot = telebot.TeleBot('1744485725:AAGSyPz9wu9kg9EgWEL0abqImol0_2sJyr8')

for el1 in html1.select('#content'):
    text1 = el1.select('.primaryContent ,p')[0].text

for el2 in html2.select('#content'):
    text2 = el2.select('.primaryContent ,p')[0].text

for el3 in html3.select('#content'):
    text3 = el3.select('.primaryContent ,p')[0].text

for el4 in html4.select('#content'):
    text4 = el4.select('.primaryContent ,p')[0].text

for el5 in html5.select('#content'):
    text5 = el5.select('.primaryContent ,p')[0].text

for el6 in html6.select('#content'):
    text6 = el6.select('.primaryContent ,p')[0].text

for el7 in html7.select('#content'):
    text7 = el7.select('.primaryContent ,p')[0].text

for el8 in html8.select('#content'):
    text8 = el8.select('.primaryContent ,p')[0].text

for el9 in html9.select('#content'):
    text9 = el9.select('.primaryContent ,p')[0].text

for el10 in html10.select('#content'):
    text10 = el10.select('.primaryContent ,p')[0].text

for el11 in html11.select('#content'):
    text11 = el11.select('.primaryContent ,p')[0].text

for el12 in html12.select('#content'):
    text12 = el12.select('.primaryContent ,p')[0].text

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»

    if message.text == "Привет":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac1')

        # И добавляем кнопку на экран

        keyboard.add(key_oven)

        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac2')

        keyboard.add(key_telec)

        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac3')

        keyboard.add(key_bliznecy)

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac4')

        keyboard.add(key_rak)

        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac5')

        keyboard.add(key_lev)

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac6')

        keyboard.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac7')

        keyboard.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac8')

        keyboard.add(key_scorpion)

        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac9')

        keyboard.add(key_strelec)

        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac10')

        keyboard.add(key_kozerog)

        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac11')

        keyboard.add(key_vodoley)

        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac12')

        keyboard.add(key_ryby)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    elif message.text == "/who":

        bot.send_message(message.from_user.id, "Зто я (Максим)")

    elif message.text == "как дела":

        bot.send_message(message.from_user.id, "Нормально")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "zodiac1":
        # Формируем гороскоп

        msg1 = text1

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg1)

    elif call.data == "zodiac2":
            # Формируем гороскоп

        msg2 = text2

            # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg2)

    elif call.data == "zodiac3":
        # Формируем гороскоп

        msg3 = text3

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg3)

    elif call.data == "zodiac4":
        # Формируем гороскоп

        msg4 = text4

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg4)

    elif call.data == "zodiac5":
        # Формируем гороскоп

        msg5 = text5

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg5)

    elif call.data == "zodiac6":
        # Формируем гороскоп

        msg6 = text6

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg6)

    elif call.data == "zodiac7":
        # Формируем гороскоп

        msg7 = text7

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg7)

    elif call.data == "zodiac8":
        # Формируем гороскоп

        msg8 = text8

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg8)

    elif call.data == "zodiac9":
        # Формируем гороскоп

        msg9 = text9

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg9)

    elif call.data == "zodiac10":
        # Формируем гороскоп

        msg10 = text10

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg10)

    elif call.data == "zodiac11":
        # Формируем гороскоп

        msg11 = text11

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg11)

    elif call.data == "zodiac12":
        # Формируем гороскоп

        msg12 = text12

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg12)




if __name__ == '__main__':
    bot.polling(none_stop=True)
