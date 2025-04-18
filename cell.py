from graphics import Window, Point, Line

class Cell(): 
    def __init__(self, x1, x2, y1, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win
        

    def draw(self): 
        for wall in self.get_wall_lines():
            self.__win.draw_line(wall)


    def get_wall_lines(self): 
        walls = []
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)
        if self.has_left_wall: 
            walls.append(Line(top_left, bottom_left))
        if self.has_right_wall: 
            walls.append(Line(top_right, bottom_right))
        if self.has_top_wall: 
            walls.append(Line(top_left, top_right))
        if self.has_bottom_wall: 
            walls.append(Line( bottom_left, bottom_right))
        return walls