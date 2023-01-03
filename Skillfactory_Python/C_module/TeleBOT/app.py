import telebot
from telebot import types
from pymorphy2 import MorphAnalyzer

from time import strftime

from config import *
from extensions import *


def create_markup(base=None):  # Создание кнопок на основе валют
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for val in currencies.keys():
        if val != base:
            buttons.append(types.KeyboardButton(val.capitalize()))

    markup.add(*buttons)
    return markup


bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


@bot.message_handler(commands=['start', 'help'])  # Команда с описанием доступных команд
def help(message: telebot.types.Message):
    text = '\nУвидеть список всех доступных валют: /values\nНачать конвертацию валют: /convert'
    bot.send_message(message.chat.id, f'Welcome, {message.chat.first_name}! {text}')


@bot.message_handler(commands=['values'])  # Команда со списком доступных валют
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currencies.keys():
        text = '\n'.join((text, key.capitalize()))
    bot.send_message(message.chat.id, text)
    print(f'{strftime("%H:%M:%S")}\t{message.chat.first_name} {message.chat.last_name}'
          f'({message.chat.username}) запросил список доступных валют.')


@bot.message_handler(commands=['convert'])  # Команда конвертации валют
def convert(message: telebot.types.Message):
    text = 'Выберите валюту, из которой конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup())
    bot.register_next_step_handler(message, quote_handler)  # Ждём следующего сообщения от пользователя


def quote_handler(message: telebot.types.Message):
    quote = message.text.strip().lower()
    text = 'Выберите валюту, в которую конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup(quote))  # Убираем валюту, выбранную ранее
    bot.register_next_step_handler(message, base_handler, quote)  # Ждём следующего сообщения от пользователя


def base_handler(message: telebot.types.Message, quote):
    base = message.text.strip().lower()
    text = 'Выберите количество конвертируемой валюты:'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, quote, base)  # Ждём следующего сообщения от пользователя


def amount_handler(message: telebot.types.Message, quote, base):
    amount = message.text.strip().lower().replace(",", ".")
    try:
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    else:
        text = f'Цена: {amount} ' \
               f'{MorphAnalyzer().parse(quote)[0].make_agree_with_number(float(amount)).word} в ' \
               f'{MorphAnalyzer().parse(base)[0].inflect({"plur", "loct"})[0]} - {total_base}'
        bot.send_message(message.chat.id, text)  # Просклоняли ответное сообщение пользователю
        print(f'{strftime("%H:%M:%S")}\t{message.chat.first_name} {message.chat.last_name}'
              f'({message.chat.username}) конвертировал валюту.')


if __name__ == '__main__':
    print(f'{strftime("%H:%M:%S")}\tBot запущен...')
    bot.polling(none_stop=True)
    print(f'{strftime("%H:%M:%S")}\tBot отключён...')
