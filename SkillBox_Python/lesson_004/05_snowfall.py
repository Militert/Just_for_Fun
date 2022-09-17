# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# for _ in range(N):
#     start_point = sd.get_point(sd.random_number(150, 1000), sd.random_number(150, 600))
#     length = sd.random_number(20, 50)
#     fa = sd.random_number(45, 75) / 100
#     fb = sd.random_number(15, 40) / 100
#     fc = sd.random_number(50, 70)
#     sd.snowflake(center=start_point, length=length, factor_a=fa, factor_b=fb, factor_c=fc)


def snow(x, y, lng):
    sd.start_drawing()
    fa = sd.random_number(45, 75) / 100
    fb = sd.random_number(15, 40) / 100
    fc = sd.random_number(50, 70)
    while True:
        sd.snowflake(center=sd.get_point(x, y), length=lng, color=sd.COLOR_WHITE,
                     factor_a=fa, factor_b=fb, factor_c=fc)
        sd.sleep(0.1)
        sd.snowflake(center=sd.get_point(x, y), length=lng, color=sd.background_color,
                     factor_a=fa, factor_b=fb, factor_c=fc)
        y -= sd.random_number(10, 30)
        x += sd.random_number(-40, 40)

        sd.finish_drawing()
        if y < 30:
            sd.snowflake(center=sd.get_point(x, y), length=lng, color=sd.COLOR_WHITE,
                         factor_a=fa, factor_b=fb, factor_c=fc)
            break
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


while True:
    length = sd.random_number(20, 50)
    Y = 900
    X = sd.random_number(50, 1000)
    snow(x=X, y=Y, lng=length)
    if sd.user_want_exit():
        break

sd.start_drawing()
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
