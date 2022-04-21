from turtle import Turtle


class Middle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.line_segments = []
        self.create_line()

    def create_line(self):
        y = 380
        for _ in range(17):
            self.line_segment = Turtle()
            self.line_segment.penup()
            self.line_segment.shape("square")
            self.line_segment.shapesize(1, 0.3)
            self.line_segment.color("white")
            y -= 50
            self.line_segment.goto(0, y)
            self.line_segments.append(self.line_segment)












