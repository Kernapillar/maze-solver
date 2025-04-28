import time
import random
from graphics import Window, Point
from cell import Cell

class Maze(): 
    def __init__(self, x, y, rows, cols, size_x, size_y, win=None, seed=None, extend=0, flipped=False):
        self.x = x 
        self.y = y 
        self.rows = rows if rows >= 1 else 1
        self.cols = cols if cols >= 1 else 1
        self.size_x = size_x
        self.size_y = size_y
        self._win = win
        if seed is not None: 
            random.seed(seed)
        self.entrance=[0, 0] if not flipped else [0,self.rows - 1]
        self.exit=[self.cols -1, self.rows -1] if not flipped else [self.cols -1, 0]
        self._flipped = flipped
        self._cells = self._create_cells()
        self._draw_all()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()
        if extend > 0: 
            self._extend = extend
            self.extend(extend)

    def _create_cells(self): 
        cells = []
        for i in range(self.cols):
            column = []
            for j in range(self.rows): 
                p1 = Point(self.x + (self.size_x * i), self.y + (self.size_y * j))
                p2 = Point(self.x + (self.size_x * (i + 1)), self.y + (self.size_y * (j + 1)))
                column.append(Cell(p1.x, p2.x, p1.y, p2.y, self._win))
            cells.append(column)
        return cells

    def _draw_all(self): 
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
        entrance = self._cells[self.entrance[0]][self.entrance[1]]
        exit = self._cells[self.exit[0]][self.exit[1]]
        entrance.has_left_wall = False
        entrance.draw()
        exit.has_right_wall = False
        exit.draw()

    def _break_walls_r(self, i, j): 
        current = self._cells[i][j]
        current.visited = True
        while True: 
            to_visit = self._possible_neighbors(i, j)
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

    def _possible_neighbors(self, i, j): 
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

    def _reset_visited(self): 
        for col in range(len(self._cells)): 
            for row in range(len(self._cells[col])): 
                self._cells[col][row].visited = False

    def solve(self): 
        first = self._solve_r(self.entrance[0], self.entrance[1])
        if first and self._extend > 0: 
            i = 0
            current = self._cells[self.exit[0]][self.exit[1]]
            while i < self._extend: 
                m = self.extension[i]
                current.draw_move(m._cells[m.entrance[0]][m.entrance[1]])
                current = m._cells[m.exit[0]][m.exit[1]]
                m._solve_r(m.entrance[0], m.entrance[1])
                i += 1
    
    def _solve_r(self, i, j): 
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if i == self.exit[0] and j == self.exit[1]: 
            return True
        neighbors = self._possible_neighbors(i, j)
        for neighbor in neighbors: 
            neighbor_i, neighbor_j, direction = neighbor
            neighbor_cell = self._cells[neighbor_i][neighbor_j]
            if self._wall_between(i, j, direction) == False: 
                current.draw_move(neighbor_cell)
                next = self._solve_r(neighbor_i, neighbor_j)
                if next: 
                    return True
                current.draw_move(neighbor_cell, undo=True)
        return False
        
    def _wall_between(self, i, j, d): 
        dirs = {"bottom": [0, 1], "top": [0, -1], "right": [1, 0], "left": [-1, 0]}
        x, y = dirs[d]
        current = self._cells[i][j]
        neighbor = self._cells[i + x][j + y]
        match d: 
            case "bottom": 
                return current.has_bottom_wall or neighbor.has_top_wall 
            case "top": 
                return current.has_top_wall or neighbor.has_bottom_wall 
            case "left": 
                return current.has_left_wall or neighbor.has_right_wall 
            case "right": 
                return current.has_right_wall or neighbor.has_left_wall 

    def extend(self, num): 
        self.extension = []
        x_offset = self.size_x * self.cols
        flipped =  not self._flipped
        for i in range(1, num + 1):
            new_maze = Maze(self.x + (x_offset * i), 
                            self.y, self.rows, self.cols, self.size_x, 
                            self.size_y, self._win, flipped=flipped)
            self.extension.append(new_maze)
            flipped = not flipped
    
