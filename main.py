import telebot
from decimal import *
import time
from binance.spot import Spot as Client

TOKEN = '5439314754:AAGU9_J-AqwAYPKsoYrx44aOLe40xRlWHc8'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


client = Client()
dict_of_time = {'1s': 1,
                '1m': 60,
                '3m': 180,
                '5m': 300,
                '10m': 600,
                '15m': 900,
                '20m': 1200,
                '25m': 1500,
                '30m': 1800,
                '1h': 3600,
                '2h': 7200,
                '4h': 14400,
                '6h': 21600,
                '8h': 28800,
                '12h': 36000,
                '1d': 72000}


def differences(impulse, percent, interval):
    dict1 = client.ticker_price()
    timeframe = dict_of_time[interval]
    time.sleep(timeframe)
    dict2 = client.ticker_price()
    result = []
    with open('black_list.txt') as file:
        black_list = list(map(lambda x: x.rstrip(), file.readlines()))
    for i in range(len(dict2)):
        if float(dict2[i]['price']) / float(dict1[i]['price']) > (float(impulse[:1]) / 100) + 1 and dict1[i]['symbol'] not in black_list:
            real_impulse = round((float(dict2[i]['price']) / float(dict1[i]['price']) - 1.0) * 100, 2)
            api = Client()
            symbol = dict2[i]['symbol']
            ticker_price = api.ticker_price(symbol=symbol)
            close_price = api.klines(symbol=symbol, interval=interval)[-2][4]
            onsale_price = round(Decimal(ticker_price['price']) * Decimal(1 + (int(percent[:-1]) / 100)), 12)
            s_onsale = '{0:f}'.format(onsale_price)
            res = 'Импульс ' + str(real_impulse) + ' ТФ ' + interval + ' на паре ' + symbol + '\n' + 'Цена закрытия на предыдущей свече: ' + close_price + '\n' + percent + '\n' + 'Цена на продажу: ' + s_onsale
            result.append(res)
    return result


flag = True


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет, это бот-воришка данных с Бинанса, высчитывает импульсы на нужных таймфреймах. Нажми /help")


@bot.message_handler(commands=['help'])
def helping(message):
    bot.reply_to(message, '/settings - настройка парсинга бота')


@bot.message_handler(commands=['settings'])
def settings_func(message):
    text = "Введите данные формата Искомый импульс/Процент продажи актива/Таймфрейм (5% 1% 5m)"
    bot.reply_to(message, text)


@bot.message_handler(commands=['stop'])
def stop(message):
    global flag
    flag = False
    text1 = 'Поиск остановлен, можете ввести новые данные: /settings'
    bot.reply_to(message, text1)


def findimpulse(settings, message, counter=0):
    global flag
    if flag:
        settings_list = settings.split()
        impulse = settings_list[0]
        percent = settings_list[1]
        interval = settings_list[2]
        if counter == 0:
            bot.reply_to(message, 'Начинаю поиск...')
        result = differences(impulse, percent, interval)
        if len(result) > 0:
            for i in result:
                bot.reply_to(message, i)

        findimpulse(settings, message, counter=1)


@bot.message_handler(func=lambda message: True)
def work(message):
    settings = message.text
    if settings[0].isdigit():
        global flag
        flag = True
        findimpulse(settings, message)
    else:
        txt = message.text
        with open('black_list.txt', 'a') as file:
            file.write(txt.upper() + '\n')
        txt = 'Пара ' + txt + ' добавлена в черный список'
        bot.reply_to(message, txt)


bot.infinity_polling()
