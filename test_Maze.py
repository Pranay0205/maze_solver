from random import seed
from Maze import Maze
import unittest
from Window import Window


class TestMaze(unittest.TestCase):

    def test_maze_create_cells(self):
        win = Window(800, 800)
        num_rows = 10
        num_cols = 12
        m1 = Maze(10, 10, num_rows, num_cols, 60, 60, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_seed_1(self):
        win = Window(800, 800)
        num_rows = 10
        num_cols = 10
        m2 = Maze(10, 10, num_rows, num_cols, 50, 50, win, 5)

    def test_maze_constructor_negative_dimensions(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, -5, -5, 40, 40)

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()
