from windows.window import Window
from maze.cell import Cell
from maze.maze import Maze

def main():
    win = Window(800,600)
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
    m1._break_entrance_and_exit()
    win.wait_for_close()

if __name__ == "__main__":
    main()