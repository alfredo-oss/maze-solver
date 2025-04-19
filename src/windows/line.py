from tkinter import Canvas

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y2, fill=fill_color, width=2)
        