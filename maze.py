import time
from graphics import Window, Point
from cell import Cell

class Maze(): 
    def __init__(self, x, y, rows, cols, size_x, size_y, win):
        self.x = x
        self.y = y
        self.rows = rows
        self.cols = cols
        self.size_x = size_x
        self.size_y = size_y
        self._win = win
        self._create_cells()

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
        cell.draw()
        self._animate()

    def _animate(self): 
        self._win.redraw()
        time.sleep(0.05)