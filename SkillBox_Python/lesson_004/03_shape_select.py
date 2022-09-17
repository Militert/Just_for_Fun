# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

dict_of_shape = {0: [120, "Треугольник"], 1: [90, "Четырёхугольник"],
                 2: [72, "Пятиугольник"], 3: [60, "Шестиугольник"],
                 4: [45, "Восьмиугольник"]}
print('Возможные фигуры:')
for key, val in enumerate(dict_of_shape.values()):
    print(f'{key} : {val[1]}')
while True:
    user_shape = int(input('Введите желаемую фигуру > '))
    if 0 < user_shape > 4:
        print('Вы ввели некорректный номер!')
    else:
        break


def figure_draw(start_point, length, width, angle=90):
    first = sd.get_vector(start_point=start_point, angle=0, length=length, width=width)
    first.draw()
    for figure in range(360//angle-1):
        second = sd.get_vector(start_point=first.end_point, angle=angle * (figure + 1), length=length, width=width)
        second.draw()
        first = second


figure_draw(start_point=sd.get_point(300, 300), angle=dict_of_shape[user_shape][0], length=100, width=2)

sd.pause()
