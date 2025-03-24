from textwrap import fill
from tkinter import Tk, BOTH, Canvas

from Cell import Cell
from Line import Line
from Point import Point


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="white",
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

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


def main():
    print("Initializing The Maze...")
    win = Window(800, 600)

    # Test two cells aligned in different rows with more distance between them
    # First cell with no bottom wall
    cell1 = Cell(win)
    cell1.has_bottom_wall = False
    cell1.draw(50, 150, 50, 150)

    # Second cell with no top wall, placed in a different row
    cell2 = Cell(win)
    cell2.has_top_wall = False
    cell2.draw(50, 150, 250, 350)

    cell1.draw_move(cell2, False)

    win.wait_for_close()


if __name__ == "__main__":
    main()
