# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# sd.ellipse(left_bottom=sd.get_point(0, 0), right_top=sd.get_point(150, 100), color=sd.COLOR_DARK_RED, width=2)
# sd.circle(center_position=sd.get_point(40, 70), radius=8, color=sd.COLOR_DARK_YELLOW, width=1)
# sd.circle(center_position=sd.get_point(110, 70), radius=8, color=sd.COLOR_DARK_YELLOW, width=1)
# sd.lines([sd.get_point(20, 50), sd.get_point(50, 25),
#           sd.get_point(100, 25), sd.get_point(130, 50)],
#          color=sd.COLOR_DARK_YELLOW, width=1)


def draw_smile(x, y, color):
    sd.ellipse(left_bottom=sd.get_point(x, y), right_top=sd.get_point(x + 150, y + 100), color=color, width=2)
    sd.circle(center_position=sd.get_point(x + 40, y + 70), radius=8, color=color, width=1)
    sd.circle(center_position=sd.get_point(x + 110, y + 70), radius=8, color=color, width=1)
    sd.lines(point_list=[sd.get_point(x + 20, y + 50), sd.get_point(x + 50, y + 25), sd.get_point(x + 100, y + 25),
                         sd.get_point(x + 130, y + 50)], color=color, width=1)


for _ in range(110):
    draw_smile(x=sd.randint(0, 450), y=sd.randint(0, 450), color=sd.random_color())

sd.pause()
