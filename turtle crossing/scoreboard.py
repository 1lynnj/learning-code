from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-290, 270)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("Courier", 24, 'normal'))

    def update_level(self):
        self.level += 1
        self.scoreboard()

    def game_over(self):
        self.goto(-200, 0)
        self.write("Splat! Game Over!", font=("Courier", 40, 'normal'))
        self.color('black')



