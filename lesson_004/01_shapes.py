# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle(start_point, length, angle=120):
#     v1 = sd.get_vector(start_point=start_point, angle=0, length=length, width=2)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle, length=length, width=2)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle * 2, length=length, width=2)
#     v3.draw()
#
#
# triangle(start_point=sd.get_point(300, 300), length=200)
#
# def square(start_point, length, angle=90):
#     v1 = sd.get_vector(start_point=start_point, angle=0, length=length, width=2)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle, length=length, width=2)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle * 2, length=length, width=2)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle * 3, length=length, width=2)
#     v4.draw()
#
#
# def pentagon(start_point, length, angle=72):
#     v1 = sd.get_vector(start_point=start_point, angle=0, length=length, width=2)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle, length=length, width=2)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle * 2, length=length, width=2)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle * 3, length=length, width=2)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle * 4, length=length, width=2)
#     v5.draw()
#
#
# def hexagon(start_point, length, angle=60):
#     v1 = sd.get_vector(start_point=start_point, angle=0, length=length, width=2)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle, length=length, width=2)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle * 2, length=length, width=2)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle * 3, length=length, width=2)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle * 4, length=length, width=2)
#     v5.draw()
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle * 5, length=length, width=2)
#     v6.draw()
#
#
# hexagon(start_point=sd.get_point(200, 200), length=200)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


def figure_draw(start_point, length, width, angle=90):
    first = sd.get_vector(start_point=start_point, angle=0, length=length, width=width)
    first.draw()
    print(first.end_point)
    for figure in range(360//angle-1):
        second = sd.get_vector(start_point=first.end_point, angle=angle * (figure + 1), length=length, width=width)
        second.draw()
        first = second
        print(first.end_point)

    last = sd.get_vector(start_point=first.end_point, angle=-angle, length=2, width=2)
    last.draw(color=(0, 8, 98))


figure_draw(start_point=sd.get_point(300, 300), angle=90, length=100, width=2)


# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
