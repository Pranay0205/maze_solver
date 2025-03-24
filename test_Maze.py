from Maze import Maze
import unittest
from Window import Window


class TestMaze(unittest.TestCase):

    win = Window(800, 800)

    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 80, 80, self.win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_constructor_valid_input(self):
        num_rows = 5
        num_cols = 5
        m2 = Maze(10, 10, num_rows, num_cols, 50, 50, self.win)
        self.assertEqual(m2.num_rows, num_rows)
        self.assertEqual(m2.num_cols, num_cols)
        self.assertEqual(m2.cell_size_x, 50)
        self.assertEqual(m2.cell_size_y, 50)
        self.assertEqual(m2._x1, 10)
        self.assertEqual(m2._y1, 10)

    def test_maze_constructor_zero_cells(self):
        num_rows = 0
        num_cols = 0
        m4 = Maze(0, 0, num_rows, num_cols, 40, 40, self.win)
        self.assertEqual(len(m4._cells), 0)

    def test_maze_constructor_negative_dimensions(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, -5, -5, 40, 40, self.win)


if __name__ == "__main__":
    unittest.main()
