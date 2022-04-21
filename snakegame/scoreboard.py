from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:  # high_scores is a variable name
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

