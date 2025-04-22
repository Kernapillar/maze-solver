from graphics import Window, Point, Line

class Cell(): 
    def __init__(self, x1, x2, y1, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.center = self.get_center()
        self.visited = False

    def get_center(self): 
        x = (self._x1 + self._x2)/2
        y = (self._y1 + self._y2)/2
        return Point(x, y)
        

    def draw(self): 
        walls, empty = self.get_wall_lines()
        for wall in walls:
            self._win.draw_line(wall)
        for wall in empty:
            self._win.draw_line(wall, "white")

    def draw_move(self, to_cell, undo=False): 
        p1 = self.center
        p2 = to_cell.center
        color = "red" if not undo else "grey"
        self._win.draw_line(Line(p1, p2), fill_color=color)


    def get_wall_lines(self): 
        walls = []
        empty = []
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall: 
            walls.append(Line(top_left, bottom_left))
        else: 
            empty.append(Line(top_left, bottom_left))
        if self.has_right_wall: 
            walls.append(Line(top_right, bottom_right))
        else: 
            empty.append(Line(top_right, bottom_right))
        if self.has_top_wall: 
            walls.append(Line(top_left, top_right))
        else: 
            empty.append(Line(top_left, top_right))
        if self.has_bottom_wall: 
            walls.append(Line( bottom_left, bottom_right))
        else: 
            empty.append(Line( bottom_left, bottom_right))
        return walls, empty