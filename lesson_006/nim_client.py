from nim_serv import put_stones, take_stone, chek_heap, is_game_over
from termcolor import cprint


put_stones()
user_number = 1
while True:
    cprint('Текущая позиция:', color='red')
    cprint(chek_heap(), color='blue')
    cprint(f'Ходит {user_number} игрок', color='red')
    position = int(input('Из какой кучи берём? '))
    quantity = int(input('Сколько берем? '))
    take_stone(position=position, quantity=quantity)
    if is_game_over():
        break
    user_number = 2 if user_number == 1 else 1
cprint(f'Выйграл игрок {user_number}!', on_color='yellow')
