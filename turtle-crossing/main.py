from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from cars import Car

screen = Screen()
screen.setup(600, 600)
screen.title("Lynn's Turtle Crossing Game")
screen.tracer(0)  # turns off auto animation

player = Player()
car = Car()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_turtle, "Up")

scoreboard.scoreboard()

play_game = True
while play_game:
    time.sleep(car.car_speed)
    screen.update()  # manually update screen (auto animation off)

    car.create_car()
    car.move_cars()

    for a in car.all_cars:
        if player.distance(a) < 20 and (player.ycor() - car.ycor()) < 10:
            play_game = False
            scoreboard.game_over()

    if player.ycor() > 280:
        scoreboard.update_level()
        player.reset_player()
        car.increase_speed()


screen.exitonclick()
