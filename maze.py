import time
import random
from graphics import Window, Point
from cell import Cell

class Maze(): 
    def __init__(self, x, y, rows, cols, size_x, size_y, win=None, seed=None, test=False):
        self.x = x 
        self.y = y 
        self.rows = rows if rows >= 1 else 1
        self.cols = cols if cols >= 1 else 1
        self.size_x = size_x
        self.size_y = size_y
        self._win = win
        if seed is not None: 
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        if test is not True: 
            self._break_walls_r(0, 0)

    def _create_cells(self): 
        self._cells = []
        for i in range(self.cols):
            column = []
            for j in range(self.rows): 
                p1 = Point(self.x + (self.size_x * i), self.y + (self.size_y * j))
                p2 = Point(self.x + (self.size_x * (i + 1)), self.y + (self.size_y * (j + 1)))
                column.append(Cell(p1.x, p2.x, p1.y, p2.y, self._win))
            self._cells.append(column)
        for i in range(len(self._cells)): 
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j) 
                
    
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        if self._win is not None:
            cell.draw()
            self._animate()

    def _animate(self): 
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self): 
        if self._win is None: 
            return
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        entrance.has_top_wall = False
        entrance.draw()
        exit.has_bottom_wall = False
        exit.draw()

    def _break_walls_r(self, i, j): 
        current = self._cells[i][j]
        current.visited = True
        while True: 
            to_visit = self.possible_neighbors(i, j)
            if len(to_visit) == 0: 
                self._draw_cell(i, j)
                return
            else: 
                direction = random.choice(to_visit)
                i2, j2, d2 = direction
                neighbor = self._cells[i2][j2]
                match d2: 
                    case "bottom": 
                        current.has_bottom_wall = False
                        neighbor.has_top_wall = False
                    case "top": 
                        current.has_top_wall = False
                        neighbor.has_bottom_wall = False
                    case "left": 
                        current.has_left_wall = False
                        neighbor.has_right_wall = False
                    case "right": 
                        current.has_right_wall = False
                        neighbor.has_left_wall = False
                self._break_walls_r(i2, j2)

    def possible_neighbors(self, i, j): 
        neighbors = []
        directions = [[0, 1, "bottom"], [0, -1, "top"], [1, 0, "right"], [-1, 0, "left"]]
        for dir in directions: 
            x, y, d = dir
            new_i = i + x
            new_j = j + y
            if new_i < 0 or new_j < 0 or new_i >= self.cols or new_j >= self.rows or self._cells[new_i][new_j].visited: 
                continue
            neighbors.append([new_i, new_j, d])
        return neighbors
