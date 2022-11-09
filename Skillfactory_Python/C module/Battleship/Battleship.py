from random import randint
from time import sleep
from abc import ABC, abstractmethod


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы доски!"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Нельзя стрелять по этим координатам!"


class ArrangementWrongException(BoardException):  # Ошибка некорректного расположения
    pass


class Dot:  # Класс координат
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):  # Определяет поведение оператора равенства или вхождения
        return self.x == other.x and self.y == other.y

    def __repr__(self):  # Вывод координат
        return f'({self.x}, {self.y})'


class Ship:  # Класс корабля
    def __init__(self, bow: Dot, lives: int, orientation: int):
        self.bow = bow
        self.length = lives
        self.orientation = orientation
        self.lives = lives

    @property
    def dots(self):  # Метод описания координат корабля
        ship_coords = []
        for i in range(self.length):
            x = self.bow.x
            y = self.bow.y

            if self.orientation == 0:  # Вертикальное расположение
                x += i

            elif self.orientation == 1:  # Горизонтальное расположение
                y += i

            ship_coords.append(Dot(x, y))
        return ship_coords

    def check_shot(self, shot: Dot):  # Проверка выстрела по координатам корабля
        return shot in self.dots


class Board:  # Класс доски
    def __init__(self, hidden=False, size=6):
        self.size = size
        self.hidden = hidden

        self.count = 0
        self.busy_coords = []
        self.ships = []
        self.play_field = [['~' for _ in range(size)] for _ in range(size)]  # Создание шаблона игрового поля

    def add_ship(self, ship):  # Метод добавления корабля на доску
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy_coords:
                raise ArrangementWrongException()
        for dot in ship.dots:
            self.play_field[dot.x][dot.y] = "■"
            self.busy_coords.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, circuit=False):  # Заполнение контура подбитого корабля
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dot in ship.dots:
            for dx, dy in near:
                current = Dot(dot.x + dx, dot.y + dy)
                if not (self.out(current)) and current not in self.busy_coords:
                    if circuit:
                        self.play_field[current.x][current.y] = "."
                    self.busy_coords.append(current)

    def __str__(self):
        result = "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.play_field):
            result += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hidden:  # Скрывает от игрока корабли противника
            result = result.replace("■", "~")
        return result

    def out(self, dot):  # Проверка точки на нахождение в игровом поле
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def shot(self, dot):  # Метод выстрела
        if self.out(dot):
            raise BoardOutException()

        if dot in self.busy_coords:
            raise BoardUsedException()

        self.busy_coords.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.lives -= 1
                self.play_field[dot.x][dot.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, circuit=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.play_field[dot.x][dot.y] = "T"
        print("Мимо!")
        return False

    def begin(self):
        self.busy_coords = []  # Изначально необходим для хранения соседних точек
        # а в дальнейшем для хранения координат выстрелов


class Player(ABC):   # Абстрактный класс игрока
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    @abstractmethod  # Метод, который необходимо будет переопределить у каждого наследника
    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):   # Класс противника
    def ask(self):
        dot = Dot(randint(0, 5), randint(0, 5))
        print('Противник думает.', end='')
        for _ in range(randint(2, 5)):
            sleep(1)
            print('.', end='')

        print(f"\nХод противника: {dot.x + 1} {dot.y + 1}")
        return dot


class User(Player):   # Класс игрока
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)


class Game:  # Класс игры
    def __init__(self, size=6):
        self.size = size
        player = self.random_board()
        comp = self.random_board()
        comp.hidden = True

        self.ai = AI(comp, player)
        self.user = User(player, comp)

    def random_board(self):  # Если расположить случайным образом не удалось, цикл перезапускается
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):  # Попытка случайного расположения кораблей
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for le in lens:
            while True:
                attempts += 1
                if attempts > 5000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), le, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except ArrangementWrongException:
                    pass
        board.begin()
        return board

    @staticmethod
    def greet():  # приветствие
        print('     Приветствуем вас     ')
        print('         в игре           ')
        print('       Морской бой        ')
        print('===========================')
        print('    Формат ввода: X Y     ')
        print('     X - номер строки     ')
        print('     Y - номер столбца    ')
        print('===========================')
        print('Игровые обозначения:      ')
        print('■ - корабль               ')
        print('X - подбитый корабль      ')
        print('. - область вокруг подбитого корабля')
        print('~ - не проверенная область')
        print('T - промах                ')

    def loop(self):
        num = 0
        while True:
            print("-" * 27)
            print("Доска пользователя:", '\t' * 5, end='Доска противника:')
            print('\n  | 1 | 2 | 3 | 4 | 5 | 6 |', '\t' * 3, end='  | 1 | 2 | 3 | 4 | 5 | 6 |')
            for i in range(len(self.user.board.play_field)):
                print(f"\n{i + 1} | " + " | ".join(self.user.board.play_field[i]) + " |", '\t' * 3, end='')
                if self.ai.board.hidden:
                    print(f"{i + 1} | " + " | ".join(self.ai.board.play_field[i]).replace("■", "~") + " |", end='')
                else:
                    print(f"{i + 1} | " + " | ".join(self.ai.board.play_field[i]) + " |", end='')
            print()

            if num % 2 == 0:
                print("-" * 27)
                print("Ходит пользователь!")
                repeat = self.user.move()
            else:
                print("-" * 27)
                print("Ходит противник!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 27)
                print("Пользователь выиграл!")
                break

            if self.user.board.count == 7:
                print("-" * 27)
                print("Противник выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


if __name__ == '__main__':
    game = Game()
    game.start()