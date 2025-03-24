from Maze import Maze
from Window import Window


class TestMaze():

    def test_maze_initialization(self):
        win = Window(800, 800)
        maze = Maze(25, 25, 10, 10, 75, 75, win)
        maze._create_cells()
        win.wait_for_close()


if __name__ == '__main__':
    test = TestMaze()
    test.test_maze_initialization()
