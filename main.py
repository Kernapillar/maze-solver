from graphics import Window, Point, Line

def main(): 
    win = Window(800, 600)
    p1 = Point(100, 100)  # 100px from left, 100px from top
    p2 = Point(700, 500)  # 700px from left, 500px from top
    p3 = Point(700, 100)  # 100px from left, 100px from top
    p4 = Point(100, 500)  # 700px from left, 500px from top
    line = Line(p1, p2)
    line2 = Line(p3, p4)
    win.draw_line(line)
    win.draw_line(line2)
    win.wait_for_close()

main()