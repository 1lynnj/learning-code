from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Lynn's Snake Game")
screen.tracer(0)  # displays animation

snake = Snake()
score = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.add_bodypart()

    # detect collision with wall
    if snake.snake_head.xcor() < -295 or snake.snake_head.xcor() > 295 or snake.snake_head.ycor() < -295 or \
        snake.snake_head.ycor() > 295:
        score.reset()
        snake.reset()


    # detect collision with tail
    for i in snake.snake_bodyparts[1:]:
        if snake.snake_head.distance(i) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
