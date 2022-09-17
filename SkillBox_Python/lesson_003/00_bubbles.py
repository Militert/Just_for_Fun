# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# for radius in range(50, 80, 10):
#     point = sd.get_point(300, 300)
#     sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def bubble(point, step, color=sd.COLOR_DARK_YELLOW):

    for _ in range(3):
        step += 10
        sd.circle(center_position=point, radius=step)


# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 300)
#     radius = 50
#
#     bubble(point=point, step=radius)

# Нарисовать три ряда по 10 пузырьков
# for y in range(300, 600, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         radius = 50
#
#         bubble(point=point, step=radius)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(101):
    point = sd.random_point()
    color = sd.random_color()
    for radius in range(random.randint(30, 60), random.randint(60, 90), 10):
        sd.circle(center_position=point, radius=radius, color=color)


sd.pause()
