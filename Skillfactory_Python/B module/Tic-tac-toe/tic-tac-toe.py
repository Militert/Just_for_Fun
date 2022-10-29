'''
Игру легко доработать для поля большей размерности
'''
play_field = [[' ' for _ in range(3)] for _ in range(3)]  # генерируем игровое поле
winner = None  # победитель
Separator = '==========================='


def greet():  # приветствие
    print('     Приветствуем вас     ')
    print('         в игре           ')
    print('     Крестики-нолики      ')
    print(Separator)
    print('    Формат ввода: X Y     ')
    print('     X - номер строки     ')
    print('     Y - номер столбца    ')
    print(Separator)


def rendering(field: list):  # отрисовка игрового поля
    print(' ', end=' | ')
    [print(f'{i}', end=' | ') for i in range(len(field))]
    print(f'\n---{"-" * 4 * len(play_field)}')
    for raw in range(len(field)):
        print(raw, end=' | ')
        for col in field[raw]:
            print(col, end=' | ')
        print(f'\n---{"-" * 4 * len(play_field)}')
    return '\n' + Separator


def checking_free_moves(field: list):   # проверка на возможность хода
    temp = []
    for raw in field:
        temp.extend(raw)
    if ' ' in temp:
        return True


def game_description(func):  # разделитель между ходами(можно было не использовать, добавил что б попрактиковаться)
    def wrapper(*args, **kwargs):
        print(f'Результат хода:')
        return rendering(func(*args, **kwargs))
    print(Separator)
    return wrapper


@game_description
def step(x: int, y: int, player: int):  # игрок player делает свой ход по коорддинатам x и y
    if player:
        play_field[x][y] = '0'
    else:
        play_field[x][y] = 'X'
    return play_field


def checker_raw(field: list, player: int):  # проверка победителя по строке
    global winner
    for raw in field:
        if all([i == 'X' for i in raw]) or all([i == '0' for i in raw]):
            winner = players[player]
            return winner


def checker_col(field: list, player: int):  # проверка победителя по столбцу
    global winner
    temp = []
    for raw in range(len(field)):
        for col in range(len(field[raw])):
            temp.append(field[col][raw])
        if all([i == 'X' for i in temp]) or all([i == '0' for i in temp]):
            winner = players[player]
            return winner
        else:
            temp = []


def checker_diag(field: list, player: int):  # проверка победителя по основной диагонали
    global winner
    temp = []
    for raw in range(len(field)):
        for col in range(len(field[raw])):
            if raw == col:
                temp.append(field[raw][col])
    if all([i == 'X' for i in temp]) or all([i == '0' for i in temp]):
        winner = players[player]
        return winner


def checker_second_diag(field: list, player: int):  # проверка победителя по побочной диагонали
    global winner
    temp = []
    for raw in range(len(field)):
        temp.append(field[raw][-raw - 1])
    if all([i == 'X' for i in temp]) or all([i == '0' for i in temp]):
        winner = players[player]
        return winner


def main_checker(field: list, player: int):  # проверка по всем направлениям
    checker_raw(field=field, player=player)
    checker_col(field=field, player=player)
    checker_diag(field=field, player=player)
    checker_second_diag(field=field, player=player)


if __name__ == "__main__":
    greet()
    players = [input(f'Введите имя {i + 1} игрока: ') for i in range(2)]  # запрашиваем имена игроков
    while checking_free_moves(field=play_field):
        if winner:
            break
        for player in range(len(players)):
            if winner:
                break
            print(f'Ходит игрок - {player + 1}')
            while checking_free_moves(field=play_field):
                try:
                    x, y = map(int, input(f'{players[player]}, введите координаты Вашего хода через пробел: ').split())
                    if x < 0 or y < 0 or x > 2 or y > 2 or type(x) is not int or type(y) is not int:
                        print('Некорректные координаты :( Попробуйте еще раз.')
                    elif play_field[x][y] != ' ':
                        print('Данный ход уже использовался')
                    else:
                        break
                except ValueError:
                    print('Некорректные координаты :( Попробуйте еще раз.')
            print(step(x=x, y=y, player=player))
            main_checker(field=play_field, player=player)

if not (checking_free_moves(field=play_field) and winner):
    print('Ничья :)')
else:
    print(f'Победил - {winner}')
