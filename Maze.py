import random
import time
from turtle import pos
from Cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if num_cols < 0 or num_rows < 0:
            raise ValueError(
                "Number of rows and columns must be positive integers.")
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed
        if self._seed is not None:
            random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        # Create a 2D array of cells
        self._cells = []
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        # Draw each cell after creation
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + self.cell_size_x * i
        x2 = x1 + self.cell_size_x
        y1 = self._y1 + self.cell_size_y * j
        y2 = y1 + self.cell_size_y
        # Draw the cell using the corner coordinates
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # Remove the top wall of the first cell (entrance)
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        # Remove the bottom wall of the last cell (exit)
        self._cells[self.num_cols - 1][self.num_rows -
                                       1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1,  self.num_rows - 1)

    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True

        while (True):
            possible_directions = []

            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j - 1, "up"))

            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j, "right"))

            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1, "down"))

            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j, "left"))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return

            next_i, next_j, direction = random.choice(possible_directions)

            if direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            if direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            if direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False

            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
