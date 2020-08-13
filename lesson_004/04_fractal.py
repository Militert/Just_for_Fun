# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
point_0 = sd.get_point(300, 0)


def draw_branches(start_point, angle, length, delta):
    while length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
    v1.draw()
    start_point = v1.end_point
    length = int(length * sd.random_number(6, 9)/10)
    delta = int(sd.random_number(delta * 6, delta * 14)/10)
    draw_branches(start_point=start_point, angle=angle - delta, length=length, delta=delta)
    draw_branches(start_point=start_point, angle=angle + delta, length=length, delta=delta)


for delta in range(10, 51, 10):
    draw_branches(start_point=sd.get_point(600, 0), angle=90, length=150, delta=delta)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
