import json

import telebot
import requests

TELEGRAM_TOKEN = ''
CRYPTOCOMPARE_TOKEN = ''

try:  # пытаюсь получить токен Telegram, который лежит в файле Telegram_token.txt
    with open('Telegram_token.txt', 'r') as token:
        TELEGRAM_TOKEN = token.read().strip()
except FileNotFoundError:
    print('Токен не найден')

try:  # пытаюсь получить токен Cryptocompare, который лежит в файле Cryptocompare_token.txt
    with open('Cryptocompare_token.txt', 'r') as token:
        CRYPTOCOMPARE_TOKEN = token.read().strip()
except FileNotFoundError:
    print('Токен не найден')

currencies = {'рубль': 'RUB',
              'доллар': 'USD',
              'эфириум': 'ETH',
              'биткоин': 'BTC'}

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> <в какую валюту перевести> ' \
           '<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.send_message(message.chat.id, f'Welcome, {message.chat.first_name}! {text}')


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currencies.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split()
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currencies[quote]}&tsyms={currencies[base]}')
    total_base = json.loads(r.content)[currencies[base]]
    text = f'Цена {amount} {quote} в {base} - {total_base * amount}'
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    print(f'Bot запущен...')
    bot.polling(none_stop=True)
    print(f'Bot отключён...')
