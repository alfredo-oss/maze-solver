from maze.cell import Cell
from windows.window import Window
from typing import List, Optional
import time
import random
from collections import deque

class Maze:
    def __init__(self, x1: float, y1: float, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window, seed: Optional[int] = None):
        self.__x1 = x1
        self.__y1 = y1 
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = self._create_cells(self.__num_rows, self.__num_cols)
        self._break_walls_r(0,0)
        if seed:
            random.seed(seed)

    def _create_cells(self, num_rows: int, num_cols: int) -> List[List[Cell]]:
        result = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        base_y = self.__y1
        for row in range(num_rows):
            base_y = base_y + self.__cell_size_y
            base_x = self.__x1
            for col in range(num_cols):
                cell = Cell(base_x, base_y, base_x + self.__cell_size_x, base_y + self.__cell_size_y)
                cell.draw(self.__win.canvas)
                self._animate()
                result[row][col] = cell
                base_x += self.__cell_size_x
    
        return result

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw(self.__win.canvas)
        self._cells[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False
        self._cells[self.__num_rows - 1][self.__num_cols - 1].draw(self.__win.canvas)    
    
    def _break_walls_r(self, row, col):
        self._cells[row][col].visited = True
        possible_movements = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        while True:
            valid_movements = []
            for cur_row, cur_col in possible_movements:
                if self.is_valid_choice(cur_row, cur_col):
                    valid_movements.append((cur_row, cur_col))
            if not valid_movements:
                self._cells[row][col].draw(self.__win.canvas)
                self._animate()
                return
            next_row, next_col = random.choice(valid_movements)
            if next_row == row - 1 and next_col == col:  
                self._cells[row][col].has_top_wall = False
                self._cells[next_row][next_col].has_bottom_wall = False
            elif next_row == row and next_col == col - 1:
                self._cells[row][col].has_left_wall = False
                self._cells[next_row][next_col].has_right_wall = False
            elif next_row == row + 1 and next_col == col:
                self._cells[row][col].has_bottom_wall = False
                self._cells[next_row][next_col].has_top_wall = False
            elif next_row == row  and next_col == col + 1:
                self._cells[row][col].has_right_wall = False
                self._cells[next_row][next_col].has_left_wall = False
            self._cells[row][col].draw(self.__win.canvas)
            self._cells[next_row][next_col].draw(self.__win.canvas)
            self._animate()
            self._break_walls_r(next_row, next_col)
                
    def is_valid_choice(self, row, col):
         if (min(row, col) < 0 or row == self.__num_rows or col == self.__num_cols or self._cells[row][col].visited):
             return False
         else:
             return True
