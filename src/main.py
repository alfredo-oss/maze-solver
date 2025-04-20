from windows.window import Window
from windows.line import Line
from maze.cell import Cell

def main():
    win = Window(800,600)
    
    line_one = Line(2,8,20,35)
    line_two = Line(3,9,30,55)
    line_three = Line(5,17,60,90)
    cell_one = Cell(100,100, 200, 200)
    cell_one.has_bottom_wall = False
    cell_one.has_top_wall = False
    win.draw_line(line_one, "red")
    win.draw_line(line_two, "blue")
    win.draw_line(line_three, "green")
    win.draw_cell(cell_one)
    win.wait_for_close()

if __name__ == "__main__":
    main()