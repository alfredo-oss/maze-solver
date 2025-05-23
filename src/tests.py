import unittest
from windows.window import Window
from maze.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )
if __name__ == "__main__":
    unittest.main()