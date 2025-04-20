from windows.window import Window
from maze.cell import Cell

def main():
    win = Window(800,600)
    cell_one = Cell(25, 25, 50, 50)
    cell_two = Cell(50, 50, 75, 75)
    win.draw_cell(cell_one)
    win.draw_cell(cell_two)
    win.draw_connecting_cell(cell_one, cell_two)
    win.wait_for_close()

if __name__ == "__main__":
    main()