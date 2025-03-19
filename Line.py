class Line:
    def __init__(self, start_point, end_point):
        self.x1 = start_point.x
        self.y1 = start_point.y
        self.x2 = end_point.x
        self.y2 = end_point.y

    def draw(self, canvas, fill_color: str):
        canvas.create_line(self.x1, self.y1, self.x2,
                           self.y2, fill=fill_color, width=2)
