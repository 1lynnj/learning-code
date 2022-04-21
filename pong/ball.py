from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10  # attributes to use with move function
        self.y_move = 10
        self.ball_speed = 0.1  # set to use with sleep.time() on main.py to delay manual animation

    # moving ball 10 places at a time
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # reversing direction of ball on y-axis with bounce
    def bounce_y(self):
        self.y_move *= -1

    # reversing direction of ball on x-axis with bounce and reset
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.8

    # resetting the ball position and speed after scoring a point
    def reset_ball(self):
        self.home()
        self.ball_speed = 0.1
        self.bounce_x()
