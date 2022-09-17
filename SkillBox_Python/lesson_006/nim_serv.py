from random import randint

_holder = []


def put_stones():
    global _holder
    _holder = []
    for _ in range(5):
        _holder.append(randint(1, 20))


def take_stone(position, quantity):
    if 0 <= position <= len(_holder):
        _holder[position-1] -= quantity


def chek_heap():
    return _holder


def is_game_over():
    return sum(_holder) == 0
