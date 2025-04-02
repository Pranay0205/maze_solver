from textwrap import fill
from tkinter import Tk, BOTH, Canvas
from Cell import Cell
from Line import Line
from Maze import Maze
from Point import Point


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="black",
                             width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = True

    def redraw(self):
        self.__root.update()

    def wait_for_close(self):
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False
        self.__root.destroy()

    def draw_line(self, line, fill_color="gray"):
        line.draw(self.canvas, fill_color)


def calculate_maze_parameters(window_width, window_height, num_rows, num_cols, min_margin=20, min_cell_size=20):
    # Calculate maximum possible cell sizes
    max_cell_width = (window_width - (2 * min_margin)) // num_cols
    max_cell_height = (window_height - (2 * min_margin)) // num_rows

    # Ensure minimum cell size
    cell_size_x = max(min_cell_size, max_cell_width)
    cell_size_y = max(min_cell_size, max_cell_height)

    # Calculate actual maze size
    maze_width = cell_size_x * num_cols
    maze_height = cell_size_y * num_rows

    # Calculate margins to center the maze
    margin_x = (window_width - maze_width) // 2
    margin_y = (window_height - maze_height) // 2

    return margin_x, margin_y, cell_size_x, cell_size_y


def main():
    window_width = 1280
    window_height = 720
    num_rows = 15  # Increased from 10
    num_cols = 15  # Increased from 10

    start_x, start_y, cell_size_x, cell_size_y = calculate_maze_parameters(
        window_width, window_height, num_rows, num_cols)

    win = Window(window_width, window_height)
    maze = Maze(start_x, start_y, num_rows, num_cols,
                cell_size_x, cell_size_y, win)
    maze.solve_dfs()
    win.wait_for_close()


if __name__ == "__main__":
    main()
