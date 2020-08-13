# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

dict_of_color = {0: [sd.COLOR_RED, "RED"], 1: [sd.COLOR_ORANGE, "ORANGE"], 2: [sd.COLOR_YELLOW, "YELLOW"],
                 3: [sd.COLOR_GREEN, "GREEN"], 4: [sd.COLOR_CYAN, "CYAN"], 5: [sd.COLOR_BLUE, "BLUE"],
                 6: [sd.COLOR_PURPLE, "PURPLE"]}
for key, val in enumerate(dict_of_color.values()):
    print(f'{key} : {val[1]}')
while True:
    user_color = int(input('Введите желаемый цвет > '))
    if 0 < user_color > 6:
        print('Вы ввели некорректный номер!')
    else:
        break


def figure_draw(start_point, length, width, color, angle=90):
    first = sd.get_vector(start_point=start_point, angle=0, length=length, width=width)
    first.draw(color=color)
    print(first.end_point)
    for figure in range(360//angle-1):
        second = sd.get_vector(start_point=first.end_point, angle=angle * (figure + 1), length=length, width=width)
        second.draw(color=color)
        first = second
        print(first.end_point)

    last = sd.get_vector(start_point=first.end_point, angle=-angle, length=1, width=2)
    last.draw(color=(0, 8, 98))


figure_draw(start_point=sd.get_point(300, 300), angle=72, length=100, color=dict_of_color[user_color][0], width=2)

sd.pause()
