from windows.window import Window
from windows.line import Line

def main():
    win = Window(800,600)
    
    line_one = Line(2,8,20,35)
    line_two = Line(3,9,30,55)
    line_three = Line(5,17,60,90)
    win.draw_line(line_one, "red")
    win.draw_line(line_two, "blue")
    win.draw_line(line_three, "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()