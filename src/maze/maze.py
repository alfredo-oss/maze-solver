from maze.cell import Cell
from windows.window import Window
from typing import List
import time

class Maze:
    def __init__(self, x1: float, y1: float, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = self._create_cells(self.__num_rows, self.__num_cols)


    def _create_cells(self, num_rows: int, num_cols: int) -> List[List[Cell]]:

        result = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        base_y = self.__y1
        for row in range(num_rows):
            base_y = base_y - self.__cell_size_y
            base_x = self.__x1
            for col in range(num_cols):
                result[row][col] = Cell(base_x, base_y, base_x + self.__cell_size_x, base_y - self.__cell_size_y)
                result[row][col].draw(self.__win.canvas)
                self._animate()
                base_x += self.__cell_size_x
    
        return result

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)
        


