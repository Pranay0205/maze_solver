from tkinter import Tk, BOTH, Canvas

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

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


def main():
    print("Initializing The Maze...")
    win = Window(800, 600)
    point_a = Point(10, 10)
    point_b = Point(10, 90)
    point_c = Point(45, 10)
    point_d = Point(10, 45)
    point_e = Point(45, 45)

    line = Line(point_a, point_b)
    win.draw_line(line, "red")
    line2 = Line(point_a, point_c)
    win.draw_line(line2, "red")
    line3 = Line(point_c, point_e)
    win.draw_line(line3, "red")
    line4 = Line(point_e, point_d)
    win.draw_line(line4, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
