from graphics import Window, Point, Line
from cell import Cell

def main(): 
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(200, 100)
    p4 = Point(300, 200)
    p5 = Point(100, 200)
    p6 = Point(200, 300)
    p7 = Point(300, 300)

    cell1 = Cell(p1.x, p2.x, p1.y, p2.y, win)
    cell2 = Cell(p3.x, p4.x, p3.y, p4.y, win)
    cell3 = Cell(p5.x, p6.x, p5.y, p6.y, win)
    cell4 = Cell(p2.x, p7.x, p2.y, p7.y, win)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell4)
    cell1.draw_move(cell4, undo=True)
    win.wait_for_close()

main()