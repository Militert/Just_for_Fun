#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

print(my_favorite_movies[:my_favorite_movies.find(',')])
print(my_favorite_movies[my_favorite_movies.rfind(',') + 2:])
print(my_favorite_movies[my_favorite_movies.find(',') + 2:
                         my_favorite_movies.find(',', my_favorite_movies.find(',') + 1)])
print(my_favorite_movies[my_favorite_movies.rfind(',', 0, my_favorite_movies.rfind(',')) +
                         2:my_favorite_movies.rfind(',')])
