from turtle import Turtle

class gameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-75, 0)
        self.color('white')
        self.write("Game Over", 24, font=('Courier', 24, 'normal'))

