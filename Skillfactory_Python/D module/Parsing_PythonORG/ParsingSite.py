import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

# Создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.HTML(html, lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью
# html парсера

ul = tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall
# скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # В каждом элементе находим, где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime')[:10], a.text, sep='\t')
