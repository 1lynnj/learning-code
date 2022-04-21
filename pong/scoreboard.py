from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=("Courier", 24, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self, player):
        self.goto(-200, 0)
        self.write(f"Game Over. {player} wins!", font=('Courier', 24, 'bold'))

