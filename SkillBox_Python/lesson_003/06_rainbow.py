# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
for coord in range(7):
    sd.line(start_point=sd.get_point(50 + coord * 10, 50),
            end_point=sd.get_point(500 + coord * 10, 500),
            color=rainbow_colors[coord], width=10)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# for coord in range(7):
#     sd.circle(center_position=sd.get_point(300, 0), radius=300 - coord * 20, color=rainbow_colors[coord], width=400)
# else:
#     sd.circle(center_position=sd.get_point(300, 0), radius=300 - (coord + 1) * 20, color=sd.COLOR_DARK_BLUE, width=400)

sd.pause()
