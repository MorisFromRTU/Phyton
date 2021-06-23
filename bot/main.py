from bs4 import BeautifulSoup as BS
import requests
import telebot

req = requests.get('https://yandex.ru/pogoda/podolsk')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot('1837513368:AAEohTJmfNvDvVs9Q5XnQq9m5a1S5FzMfQg')

for el in html.select('.swiper-wrapper'):
    t_day = el.select('.temp forecast-briefly__temp forecast-briefly__temp_day')[0].text
    print(t_day)

@bot.message_handler(commands=['start', 'help'])
def mes(message):
    bot.send_message(message.chat.id, 'Привет, погода на сегодня: ')
if __name__ == '__mes__':
    bot.polling(none_stop = True)

