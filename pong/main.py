from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle_line import Middle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("Let's play pong!")
screen.tracer(0)  # turn off animation >> have to manually update screen. See below
screen.bgpic("pong_background.gif")

# line = Middle()

right_paddle = Paddle((350, 0))
right_paddle.color("blue")

left_paddle = Paddle((-350, 0))
left_paddle.color("yellow")

ball = Ball()


right_score = Scoreboard((155, 260))
right_score.color("blue")
left_score = Scoreboard((-250, 260))
left_score.color("yellow")
right_score.update_scoreboard()
left_score.update_scoreboard()
score = Scoreboard((0, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, 'a')
screen.onkey(left_paddle.down, 'z')


# manual screen update requires a while loop to continue updating
game_on = True
while game_on:
    time.sleep(ball.ball_speed)  # sets delay of screen update
    screen.update()
    ball.move()


    # detect collision with top and bottom walls and bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # detect collision with paddles and bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball goes out of bounds
    if ball.xcor() > 400:
        left_score.update_score()
        ball.reset_ball()

    elif ball.xcor() < -400:
        right_score.update_score()
        ball.reset_ball()

    if right_score.score >= 5 or left_score.score >= 5:
        game_on = False
        if right_score.score > left_score.score:
            winner = "Right Player"
        else:
            winner = "Left Player"

        score.game_over(winner)


screen.exitonclick()
