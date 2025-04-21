from tkinter import Canvas

class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def draw(self, canvas: Canvas):
        if self.has_left_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2, fill="black")
        else:
            canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2, fill="white")

        if self.has_right_wall:
            canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2, fill="black")
        else:
            canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2, fill="white")

        if self.has_top_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1, fill="black")
        else: 
            canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1, fill="white")

        if self.has_bottom_wall:
            canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y2, fill="black")
        else:
            canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y2, fill="white")
    
    def draw_move(self, canvas: Canvas, to_cell, undo=False):
        origin_x = self.__x1 + (self.__x2 - self.__x1)/2
        origin_y = self.__y1 - (self.__y1 - self.__y2)/2

        destination_x = to_cell.__x1 + (to_cell.__x2 - to_cell.__x1)/2
        destination_y = to_cell.__y1 - (to_cell.__y1 - to_cell.__y2)/2
        filling = "grey" if undo else "red"
        canvas.create_line(origin_x, origin_y, destination_x, destination_y, fill=filling)