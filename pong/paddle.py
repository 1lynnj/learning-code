from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        self.speed(0)  # setting animation to null, movement of paddles with onkey press

    # moving the paddle up and down on y-axis by 20
    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
