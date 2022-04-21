from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Lynn's Snake Game")
screen.tracer(0)

snake_bodyparts = []

####Creates snake and starting point for first 3 body parts
x = 20

for _ in range(3):
    snake_body = Turtle()
    snake_body.penup()
    snake_body.color("white")
    snake_body.shape("square")
    x -= 20
    snake_body.goto(x, 0)
    snake_bodyparts.append(snake_body)


###Moves snake
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # for loop so snake body parts move together
    for snake_part in range(len(snake_bodyparts)-1, 0, -1):
        # 3 lines of code to tell the last body part (line 3) to go to position of second to last body part.
        new_x = snake_bodyparts[snake_part-1].xcor()
        new_y = snake_bodyparts[snake_part-1].ycor()
        snake_bodyparts[snake_part].goto(new_x, new_y)

    snake_bodyparts[0].forward(20)

def left():
    snake_body.setheading(0)

def right():
    snake_body.setheading(180)

def up():
    snake_body.setheading(90)

def down():
    snake_body.setheading(270)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()


















screen.exitonclick()