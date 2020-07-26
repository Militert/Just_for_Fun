# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# sd.line(start_point=sd.get_point(0, 50), end_point=sd.get_point(0, 50 + 50), color=sd.COLOR_ORANGE, width=2)

for x in range(0, 1000, 100):
    for y in range(0, 1000, 50):
        sd.line(start_point=sd.get_point(x, y), end_point=sd.get_point(x + 100, y),
                color=sd.COLOR_ORANGE, width=2)
        if y % 100 == 0:
            sd.line(start_point=sd.get_point(x, y), end_point=sd.get_point(x, y + 50),
                    color=sd.COLOR_ORANGE, width=2)
        else:
            sd.line(start_point=sd.get_point(x - 50, y), end_point=sd.get_point(x - 50, y + 50),
                    color=sd.COLOR_ORANGE, width=2)

sd.pause()
