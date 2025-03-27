from os import error
from Line import Line
from Point import Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self._win is None:
            raise ValueError("Cannot draw cell: No window reference provided")

        pointA = Point(self._x1, self._y1)
        pointB = Point(self._x2, self._y1)
        pointC = Point(self._x1, self._y2)
        pointD = Point(self._x2, self._y2)

        if self.has_left_wall:
            left_wall = Line(pointA, pointC)
            self._win.draw_line(left_wall)
        else:
            left_wall = Line(pointA, pointC)
            self._win.draw_line(left_wall, "white")

        if self.has_top_wall:
            top_wall = Line(pointA, pointB)
            self._win.draw_line(top_wall)
        else:
            top_wall = Line(pointA, pointB)
            self._win.draw_line(top_wall, "white")

        if self.has_right_wall:
            right_wall = Line(pointB, pointD)
            self._win.draw_line(right_wall)
        else:
            right_wall = Line(pointB, pointD)
            self._win.draw_line(right_wall, "white")

        if self.has_bottom_wall:
            bottom_wall = Line(pointC, pointD)
            self._win.draw_line(bottom_wall)
        else:
            bottom_wall = Line(pointC, pointD)
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell: 'Cell', undo=False):
        line_color = "gray" if undo else "red"
        start_cell_xc = abs(self._x1 + self._x2) // 2
        start_cell_yc = abs(self._y1 + self._y2) // 2

        end_cell_xc = abs(to_cell._x1 + to_cell._x2) // 2
        end_cell_yc = abs(to_cell._y1 + to_cell._y2) // 2

        start_point = Point(start_cell_xc, start_cell_yc)
        end_point = Point(end_cell_xc, end_cell_yc)

        line = Line(start_point, end_point)

        self._win.draw_line(line, line_color)

    # def __repr__(self):
    #     visited_status = "✔" if self.visited else "✘"
    #     return (f"Cell("
    #             f"x1={self._x1}, "
    #             f"x2={self._x2}, "
    #             f"y1={self._y1}, "
    #             f"y2={self._y2}, "
    #             f"visited={visited_status})\n")
