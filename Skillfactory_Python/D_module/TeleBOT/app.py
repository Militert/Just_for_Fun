import telebot
from pymorphy2 import MorphAnalyzer

from time import strftime

from config import currencies, TELEGRAM_TOKEN
from extensions import APIException, CryptoConverter


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
        text = '\n'.join((text, key.capitalize()))
    bot.send_message(message.chat.id, text)
    print(f'{strftime("%H:%M:%S")}\t{message.chat.first_name} {message.chat.last_name}'
          f'({message.chat.username}) запросил список доступных валют.')


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split()

        if len(values) > 3:
            raise APIException('Слишком много аргументов.')
        elif len(values) < 3:
            raise APIException('Слишком мало аргументов.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Цена: {amount} ' \
               f'{MorphAnalyzer().parse(quote)[0].make_agree_with_number(float(amount.replace(",", "."))).word}' \
               f' в {MorphAnalyzer().parse(base)[0].inflect({"plur", "loct"})[0]} - {total_base}'
        bot.send_message(message.chat.id, text)
        print(f'{strftime("%H:%M:%S")}\t{message.chat.first_name} {message.chat.last_name}'
              f'({message.chat.username}) конвертировал валюту.')


if __name__ == '__main__':
    print(f'{strftime("%H:%M:%S")}\tBot запущен...')
    bot.polling(none_stop=True)
    print(f'{strftime("%H:%M:%S")}\tBot отключён...')
