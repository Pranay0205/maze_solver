import time
from Cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []

    def _create_cells(self):
        self._cells = [[self._draw_cell(i, j) for i in range(self.num_cols)]
                       for j in range(self.num_rows)]

    def _draw_cell(self, i, j):
        x1 = self._x1 + self.cell_size_x * i
        x2 = x1 + self.cell_size_x
        y1 = self._y1 + self.cell_size_y * j
        y2 = y1 + self.cell_size_y

        cell = Cell(self._win)

        cell.draw(x1, x2, y1, y2)
        self._animate()
        return cell

    def _animate(self):
        # if self._win in None:
        # return
        self._win.redraw()
        time.sleep(0.05)
