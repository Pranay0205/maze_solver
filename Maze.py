import time
from Cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
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
        self._create_cells()
        self._break_entrance_and_exit()

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

        time.sleep(1)
