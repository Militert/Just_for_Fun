play_field = [[' ' for _ in range(6)] for _ in range(6)]  # генерируем игровое поле
winner = None  # победитель
Separator = '==========================='


def greet():  # приветствие
    print('     Приветствуем вас     ')
    print('         в игре           ')
    print('       Морской бой        ')
    print(Separator)
    print('    Формат ввода: X Y     ')
    print('     X - номер строки     ')
    print('     Y - номер столбца    ')
    print(Separator)

