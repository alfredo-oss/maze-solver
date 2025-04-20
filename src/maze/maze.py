from maze.cell import Cell
from windows.window import Window
from typing import List
class Maze:
    def __init__(self, x1: float, y1: float, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

    def create_cells(self, num_rows: int, num_cols: int) -> List[List[Cell]]:
        # this should be populated with the proper positioning from the beggining
        result = [[Cell(0,0,0,0)]]
