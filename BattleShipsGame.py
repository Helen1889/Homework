from random import randint

class BoardException(Exception):
    pass
class BoardOutException(BoardException):
     def __str__(self):
         return "Выстрел вне доски!"
class SameCellException(BoardException):
    def __str__(self):
        return "Сюда вы уже стреляли"
    pass
class WrongShipException(BoardException):
    pass

class Cell:
    def __init__(self,x, y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.y==other.y and self.x==other.x
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
class Ship:
    def __init__(self,cell, lifes, direction):
        self.cell=cell
        self.lifes=lifes
        self.direction=direction
    @property
    def cells(self):
        ship_cells=[]
        for j in range(self.lifes):
            cur_x= self.cell.x
            cur_y=self.cell.y

            if self.direction == 0:
                cur_x+=1
            elif self.direction == 1:
                cur_y+=1
            ship_cells.append(Cell(cur_x,cur_y))
        return ship_cells
    def is_shot(self, shot):
        return shot in self.cells


class Board:
    def __init__(self, size, hid):
        self.size=size
        self.hid = hid

        self.count = 0 #количество пораженных кораблей

        self.field = [ ["O"]* size for _ in range(size)] # Сетка поля

        self.busy=[] #Занятые точки либо кораблем либо выстрелом
        self.ships=[] # Список кораблей доски
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 | "
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) +" |"
        if self.hid == True:
            res = res.replace("K", "0")
        return res

    def out(self, c):
        return not ((0 <= c.x < self.size) and (0<=c.y < self.size))
    def contour(self, ship, verb = False):
        near = [(-1,-1), (-1,0), (-1,1),
                (0,-1), (0,0), (0,1),
                (1,-1),(1,0), (1,1)]
        for c in ship.cells:
            for dx, dy in near:
                cur = Cell(c.x+dx, c.y+dy)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y]="."
                    self.busy.append(cur)
    def add_ship(self, ship):
        for c in ship.cells:
            if self.out(c) or c in self.busy:
                raise WrongShipException()
        for c in ship.cells:
            self.field[c.x][c.y]="K"
            self.busy.append(c)

        self.ships.append(ship)
        self.contour(ship)
    def shot(self, c):
        if self.out(c):
            raise BoardOutException()
        if c in self.busy:
            raise SameCellException()
        self.busy.append(c)

        for ship in self.ships:
            if ship.is_shot(c):
                ship.lifes -=1
                self.field[c.x][c.y]="X"
                if ship.lifes == 0:
                    self.count +=1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print ("Корабль ранен!")
                    return True
            self.field[c.x][c.y]="."
            print ("Мимо!")
            return False
    def begin(self):
        self.busy =[]
    def defeat(self):
        return self.count == len(self.ships)


class Player:
    def __init__(self,board, enemy):
        self.board=board
        self.enemy=enemy
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
class AI(Player):
    def ask(self):
        c=Cell(randint(0,5), randint(0, 5))
        print(f"Ход компьютера: {c.x+1}{c.y+1}")
        return c
class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print("Введите 2 координаты! ")
                continue
            x,y = cords

            if not(x.isdigit()) or not(y.isdigit()):
                print("Введите числа! ")
                continue
            x,y = int(x),int(y)
            return Cell(x-1,y-1)
class Game:
    def __init__(self, size =6):
        self.size = size
        pl = self.random_board(False)
        co = self.random_board(True)


        self.ai=AI(co, pl)
        self.us=User(pl, co)
    def greet(self):
        print("-------------------")
        print("---Морской--бой----")
        print("-------------------")
        print("-формат ввода: х,у-")
        print("-х - номер строки--")
        print("-у - номер столбца-")

    def loop(self):
        num = 0
        while True:
            print("-"*20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-"*20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-"*20)
            if num % 2==0:
                print ("Ходит пользователь:")
                repeat = self.us.move()
            else:
                print("Ходит компьютер:")
                repeat = self.ai.move()
            if repeat:
                num -=1

            if self.ai.board.defeat():
                print("-"*20)
                print("Пользователь выиграл!")
                break

            if self.us.board.defeat():
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num +=1



    def try_board(self, hid):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(self.size, hid)
        attempts = 0
        for l in lens:
            while True:
                attempts +=1
                if attempts > 2000:
                    return None
                ship = Ship(Cell(randint(0, self.size), randint(0, self.size)), l, randint (0,1))
                try:
                    board.add_ship(ship)
                    break
                except WrongShipException:
                    pass
        board.begin()
        return board
    def random_board(self, hid):
        board = None
        while board is None:
            board = self.try_board(hid)
        return board
    def start(self):
        self.greet()
        self.loop()
g=Game()
g.start()