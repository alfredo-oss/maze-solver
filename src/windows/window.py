from tkinter import Tk, BOTH, Canvas
from windows.line import Line
from maze.cell import Cell

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze-Solver Window")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas()
        self.canvas.pack()
        self.__running = False
        

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color=fill_color)

    def draw_cell(self, cell: Cell):
        cell.draw(self.canvas)

    def draw_connecting_cell(self, origin_cell: Cell, destination_cell: Cell):
        origin_cell.draw_move(self.canvas, destination_cell)