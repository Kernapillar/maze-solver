from graphics import Window, Point, Line
from cell import Cell

def main(): 
    win = Window(800, 600)


    p1 = Point(100, 100)  
    p2 = Point(700, 500)  
    p3 = Point(700, 100)  
    p4 = Point(100, 500)  
    line = Line(p1, p2)
    line2 = Line(p3, p4)
    win.draw_line(line)
    win.draw_line(line2)
    cell = Cell(p1.x, p2.x, p1.y, p2.y, win, left_wall=False, right_wall=False)
    cell.draw()
    


    win.wait_for_close()

main()