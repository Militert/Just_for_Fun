TELEGRAM_TOKEN = ''

try:  # пытаюсь получить токен Telegram, который лежит в файле Telegram_token.txt
    with open('Telegram_token.txt', 'r') as token:
        TELEGRAM_TOKEN = token.read().strip()
except FileNotFoundError:
    print('Токен не найден')

currencies = {'рубль': 'RUB',
              'доллар': 'USD',
              'эфириум': 'ETH',
              'биткоин': 'BTC'}
