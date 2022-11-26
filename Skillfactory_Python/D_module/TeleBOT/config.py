TELEGRAM_TOKEN = '5802753971:AAHVuxWn52OrRO90p2SaSnIntjTM8LWUPoc'

# try:  # пытаюсь получить токен Telegram, который лежит в файле Telegram_token.txt
#     with open('Telegram_token.txt', 'r') as token:
#         TELEGRAM_TOKEN = token.read().strip()
# except FileNotFoundError:
#     print('Токен не найден')

currencies = {'рубль': 'RUB',
              'доллар': 'USD',
              'евро': 'EUR',
              'юань': 'CNY',
              'злотый': 'PLN',
              'тенге': 'KZT'}
