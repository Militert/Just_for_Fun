import telebot

TOKEN = ''
try:
    with open('../../Telegram_token.txt', 'r') as token:
        TOKEN = token.read().strip()
except FileNotFoundError:
    print('Файл не найден')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Welcome, {message.chat.first_name}')


@bot.message_handler(content_types=['photo'])
def rating_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


if __name__ == '__main__':
    print(f'Bot запущен...')
    bot.polling(none_stop=True)
    print(f'Bot отключён...')
