import random


class GameGrid:
    def __init__(self, row, column, win_score):
        self.row = row
        self.column = column
        self.win_score = win_score
        self.grid = [[0 for i in range(self.column)] for j in range(self.row)]

    def insert(self):
        empty = []
        insert_val = random.choice([2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4])
        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j] == 0:
                    empty.append([i, j])
        insert = random.choice(empty)
        self.grid[insert[0]][insert[1]] = insert_val

    def print_grid(self):
        print('+----' * self.column + '+')
        for row in self.grid:
            for column in row:
                if column == 0:
                    print('|{0:^4}'.format(''), end='')
                else:
                    print('|{0:^4}'.format(column), end='')
            print('|')
            print('+----' * self.column + '+')
        print("Please input Up:'w' or Left:'a' or Down:'s' or Right:'d'")

    def move_grid(self, direction):
        Grid = [[0 for i in range(self.column)] for j in range(self.row)]
        for i in range(self.row):
            nums = []
            res = []
            if direction in ['left', 'right']:
                for j in range(self.column):
                    if self.grid[i][j] != 0:
                        nums.append(self.grid[i][j])
            elif direction in ['up', 'down']:
                for j in range(self.row):
                    if self.grid[j][i] != 0:
                        nums.append(self.grid[j][i])
            if direction in ['right', 'down']:
                nums = nums[-1::-1]
            nums += [0 for i in range(self.column)]
            while len(nums):
                x = nums.pop(0)
                if x != 0 and x == nums[0]:
                    res.append(x * 2)
                    nums.pop(0)
                else:
                    res.append(x)
            match direction:
                case 'right':
                    for j in range(self.row):
                        Grid[i][j] = res[3 - j]
                case 'left':
                    for j in range(self.row):
                        Grid[i][j] = res[j]
                case 'down':
                    for j in range(self.row):
                        Grid[j][i] = res[3 - j]
                case 'up':
                    for j in range(self.row):
                        Grid[j][i] = res[j]
        return Grid

    def do_next(self, direction):
        check = self.check(direction)
        if check == 3:
            self.insert()
            self.print_grid()
        elif check == 2:
            self.print_grid()
            print('you win!')
        elif check == 1:
            self.print_grid()
        elif check == 0:
            print('game over!')

    def check(self, direction):
        Grid_up = self.move_grid('up')
        Grid_left = self.move_grid('left')
        Grid_down = self.move_grid('down')
        Grid_right = self.move_grid('right')
        if Grid_up == Grid_left and Grid_left == Grid_down and Grid_down == Grid_right:
            return 0
        match direction:
            case 'up':
                if self.grid == Grid_up:
                    return 1
                self.grid = Grid_up
            case 'left':
                if self.grid == Grid_left:
                    return 1
                self.grid = Grid_left
            case 'down':
                if self.grid == Grid_down:
                    return 1
                self.grid = Grid_down
            case 'right':
                if self.grid == Grid_right:
                    return 1
                self.grid = Grid_right
        if self.win_score in list([i for item in self.grid for i in item]):
            return 2
        return 3

    def start(self):
        global flag
        self.insert()
        self.insert()
        self.print_grid()
        while True:
            X = input()
            match X:
                case 'w':
                    self.do_next('up')
                case 'a':
                    self.do_next('left')
                case 's':
                    self.do_next('down')
                case 'd':
                    self.do_next('right')
                case '':
                    self.print_grid()


GameGrid(4, 4, 8).start()
