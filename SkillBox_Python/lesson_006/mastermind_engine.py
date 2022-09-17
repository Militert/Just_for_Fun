from random import randint


_4_random_number = []
_steps = 0


def rand_4_number():
    global _4_random_number
    _4_random_number = [randint(0, 9) for _ in range(4)]
    while True:
        if len(set(_4_random_number)) < len(_4_random_number) or _4_random_number[0] == 0:
            _4_random_number = [randint(0, 9) for _ in range(4)]
        else:
            break


def guess_number(user_number: str):
    user_input = []
    global _steps
    guess = {'Быков': 0, 'Коров': 0}

    if not user_number.isdigit():
        return 'Вы ввели не число'
    if len(user_number) != 4:
        return 'Вы ввели не 4х значное число'
    for i in user_number:
        user_input.append(int(i))

    _steps += 1
    if user_input == _4_random_number:
        print('Вы отгадали задуманное число!\nУ вас ушло на это', _steps, 'ходов')
        _steps = 0
        return 'Хотите попробовать еще раз?(Да/Нет)'
    else:
        for i in range(len(user_input)):
            if user_input[i] == _4_random_number[i]:
                guess['Быков'] += 1
            elif user_input[i] in _4_random_number:
                guess['Коров'] += 1
        for oxs, numb in guess.items():
            print(f'{oxs} - {numb}')
    return 'Попробуйте ещё раз!'


def game_over(user_number):
    user_input = []
    for i in user_number:
        user_input.append(int(i))
    return user_input == _4_random_number
