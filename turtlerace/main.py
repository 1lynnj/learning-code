from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "green", "blue", "yellow", "purple", "orange"]
turtle_names = ["luke", "jay", "dean", "cordy", "anna", "thelma"]
turtles = []
y = 175

player_bet = screen.textinput("Place your bet!",
                              "What color turtle will win the race? red / green / blue / yellow / purple / orange")
print(f"The player bet is: {player_bet}.")

for name in turtle_names:
    name = Turtle()
    turtles.append(name)
    name.shape("turtle")
    turtle_color = random.choice(colors)
    name.color(turtle_color)
    colors.remove(turtle_color)
    name.penup()
    y -= 50
    name.goto(-225, y)

race = False

if player_bet:
    race = True

while race:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            turtle_color = str(turtle.pencolor())
            if turtle_color == player_bet:
                print(f"You win! The winner is {turtle.pencolor()}.")
            else:
                print(f"You lose. The winner is {turtle.pencolor()}.")
            race = False

screen.exitonclick()

# Need to solve tie races. Currently, lists more than one as the winner and prints the
# player status for each one.
