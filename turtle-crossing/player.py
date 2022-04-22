from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)

    def move_turtle(self):
        self.forward(10)

    def reset_player(self):
        self.goto(0, -280)



# when frog reaches top of screen, reset position, increase level by 1, increase speed of cars
