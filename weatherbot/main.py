# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import requests
import telebot
from telebot import types
is_Weat = False
is_Money = False

bot = telebot.TeleBot('1837513368:AAEohTJmfNvDvVs9Q5XnQq9m5a1S5FzMfQg')
def tr(x):
    t = ''
    for i in x:
        t+=i.lower()
    return t
dates = ['1 января','2 января','3 января','4 января','5 января','6 января','7 января','8 января', '9 января', '10 января', '11 января','12 января','13 января','14 января','15 января','16 января','17 января','18 января', '19 января', '20 января','21 января','22 января','23 января','24 января','25 января','26 января','27 января','28 января', '29 января', '30 января', '31 января', '1 февраля', '2 февраля', '3 февраля', '4 февраля', '5 февраля', '6 февраля', '7 февраля', '8 февраля', '9 февраля', '10 февраля', '11 февраля', '12 февраля', '13 февраля', '14 февраля', '15 февраля', '16 февраля', '17 февраля', '18 февраля', '19 февраля', '20 февраля','21 февраля', '22 февраля', '23 февраля', '24 февраля', '25 февраля', '26 февраля', '27 февраля', '28 февраля','1 марта', '2 марта','3 марта','4 марта','5 марта','6 марта','7 марта','8 марта','9 марта','10 марта','11 марта','12 марта','13 марта','14 марта','15 марта','16 марта','17 марта','18 марта','19 марта','20 марта','21 марта','22 марта','23 марта','24 марта','25 марта','26 марта','27 марта','28 марта','29 марта','30 марта','31 марта','1 апреля','2 апреля','3 апреля','4 апреля','5 апреля','6 апреля','7 апреля','8 апреля','9 апреля','10 апреля','11 апреля','12 апреля','13 апреля','14 апреля','15 апреля','16 апреля','17 апреля','18 апреля', '19 апреля','20 апреля','21 апреля','22 апреля','23 апреля','24 апреля','25 апреля','26 апреля','27 апреля','28 апреля', '29 апреля', '30 апреля', '1 мая', '2 мая', '3 мая', '4 мая', '5 мая', '6 мая', '7 мая', '8 мая', '9 мая', '10 мая', '11 мая', '12 мая', '13 мая', '14 мая', '15 мая', '16 мая', '17 мая', '18 мая', '19 мая', '20 мая', '21 мая', '22 мая', '23 мая', '24 мая', '25 мая', '26 мая', '27 мая', '28 мая', '29 мая', '30 мая', '31 мая', '1 июня', '2 июня', '3 июня', '4 июня', '5 июня', '6 июня', '7 июня', '8 июня', '9 июня', '10 июня', '11 июня', '12 июня', '13 июня', '14 июня', '15 июня', '16 июня', '17 июня', '18 июня', '19 июня', '20 июня', '21 июня', '22 июня', '23 июня', '24 июня', '25 июня', '26 июня', '27 июня', '28 июня','29 июня','30 июня', '1 июля', '2 июля', '3 июля', '4 июля', '5 июля', '6 июля', '7 июля', '8 июля', '9 июля', '10 июля', '11 июля', '12 июля', '13 июля', '14 июля', '15 июля', '16 июля', '17 июля', '18 июля', '19 июля', '20 июля', '21 июля', '22 июля', '23 июля', '24 июля', '25 июля', '26 июля', '27 июля', '28 июля', '29 июля', '30 июля', '31 июля','1 августа','2 августа','3 августа','4 августа','5 августа','6 августа','7 августа','8 августа','9 августа','10 августа','11 августа','12 августа','13 августа','14 августа','15 августа','16 августа','17 августа','18 августа','19 августа','20 августа','21 августа','22 августа','23 августа','24 августа','25 августа','26 августа','27 августа','28 августа','29 августа','30 августа', '31 августа', '1 сентября', '2 сентября', '3 сентября', '4 сентября', '5 сентября', '6 сентября', '7 сентября', '8 сентября', '9 сентября', '10 сентября', '11 сентября', '12 сентября', '13 сентября', '14 сентября', '15 сентября', '16 сентября', '17 сентября', '18 сентября', '19 сентября', '20 сентября', '21 сентября','22 сентября', '23 сентября', '24 сентября', '25 сентября', '26 сентября', '27 сентября', '28 сентября', '29 сентября', '30 сентября', '1 октября', '2 октября', '3 октября', '4 октября', '5 октября', '6 октября', '7 октября', '8 октября', '9 октября', '10 октября', '11 октября', '12 октября', '13 октября', '14 октября', '15 октября', '16 октября', '17 октября', '18 октября', '19 октября', '20 октября', '21 октября', '22 октября', '23 октября', '24 октября', '25 октября', '26 октября', '27 октября', '28 октября', '29 октября', '30 октября', '31 октября', '1 ноября', '2 ноября', '3 ноября', '4 ноября', '5 ноября', '6 ноября', '7 ноября', '8 ноября', '9 ноября', '10 ноября', '11 ноября', '12 ноября', '13 ноября', '14 ноября', '15 ноября', '16 ноября', '17 ноября', '18 ноября', '19 ноября', '20 ноября', '21 ноября','22 ноября', '23 ноября', '24 ноября', '25 ноября', '26 ноября', '27 ноября', '28 ноября', '29 ноября', '30 ноября','1 декабря','2 декабря','3 декабря','4 декабря','5 декабря','6 декабря','7 декабря','8 декабря','9 декабря','10 декабря','11 декабря','12 декабря','13 декабря','14 декабря','15 декабря','16 декабря','17 декабря','18 декабря','19 декабря','20 декабря','21 декабря','22 декабря','23 декабря','24 декабря','25 декабря','26 декабря','27 декабря','28 декабря', '29 декабря', '30 декабря','31 декабря']
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f' Приятно познакомиться,{message.from_user.first_name}.Введи /menu, чтобы узнать обо мне побольше. ')
                          #f'Я бот, который показывает погоду. Погоду в каком горде вы хотите узнать?'
                          #f' Пожалуйста, пишите название города на английском языке и не допускайте ошибок,'
                          #f' иначе всё перестанет работать=)')
    #bot.register_next_step_handler(message, get_Content);

@bot.message_handler(commands=['menu'])
def handle_menu_help(message):
    keyboard = types.InlineKeyboardMarkup()
    key_weat = types.InlineKeyboardButton(text='Узнать погоду', callback_data='weat')
    key_money = types.InlineKeyboardButton(text='Узнать курс валют)', callback_data='money')
    keyboard.add(key_weat)
    keyboard.add(key_money)
    bot.send_message(message.from_user.id, 'Меню: ', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global is_Weat
    global is_Money
    if call.data == 'weat':
        bot.send_message(call.message.chat.id, 'Я бот, который показывает погоду. Погоду в каком горде вы хотите узнать?'
                          f' Пожалуйста, пишите название города на английском языке и не допускайте ошибок,'
                          f' иначе всё перестанет работать=)')
        is_Weat = True
    elif call.data == 'money':
        bot.send_message(call.message.chat.id, 'Я бот, который показывает курс валют, напишите мне любое сообщение..')
        is_Money = True
    elif call.data == '':
        # TODO
        pass

@bot.message_handler(content_types=['text'])
def test(message):
    if is_Weat:
        try:
            get_Content(message)
        except BaseException:
            bot.send_message(message.chat.id, 'Такого города не существует!')
    elif is_Money:
        get_Content2(message)

def get_Content2(message):
   is_Money = False
   URL_2 = 'https://yandex.ru'
   html_2 = requests.get(URL_2)
   soup_2 = BS(html_2.text, 'html.parser')
   for el in soup_2.select('.inline-stocks__content'):
       dol = el.select('.inline-stocks__value_inner')[0].text
       euro = el.select('.inline-stocks__value_inner')[1].text
   bot.send_message(message.from_user.id, f'Курс долллара на сегодня: {dol}; Курс Евро: {euro}' )


def get_Content(message):
    is_Weat = False
    city = message.text
    URL = 'https://yandex.ru/pogoda/' + tr(city)
    html = requests.get(URL)
    soup = BS(html.text, 'html.parser')
    items = soup.find_all('div', class_='forecast-briefly__day')
    global days
    days = []
    for el in items:
        days.append({
            'data': el.find('time', class_='forecast-briefly__date').get_text(),
            'temp': 'днём ' + el.find('span', class_='temp__value_with-unit').get_text() + ' °С',
            'cond': el.find('div', class_= 'forecast-briefly__condition').get_text()
        })
    today = days[1].get('data')
    global today_temp
    for i in range (len(dates)):
        if today == dates[i]:
             today_temp = i
    bot.send_message(message.from_user.id, 'Погоду на какое число в городе вы хотите узнать:')
    bot.register_next_step_handler(message, get_Data);

def get_Data(message):
    day = message.text
    if day in dates:
        for i in range (len(dates)):
            if day == dates[i]:
                day_temp = i
        element = day_temp-today_temp+1
        if element<30:
            bot.send_message(message.from_user.id, days[element].get('data') + ' - температура '+ days[element].get('temp') + '. '+ days[element].get('cond') + '.')
        else:
            bot.send_message(message.from_user.id,'Данных пока нет.')
    else:
        bot.send_message(message.from_user.id,'Такой даты не существует.')
bot.polling(none_stop = True)
