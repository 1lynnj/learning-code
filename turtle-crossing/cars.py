from turtle import Turtle
import random

COLORS = ['red', 'yellow', 'green', 'blue', 'cyan', 'orange', 'pink', 'purple', 'light green']


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y = random.randint(-250, 250)
            a_car = Turtle("square")
            a_car.penup()
            a_car.shapesize(1, 2)
            a_car.color(random.choice(COLORS))
            a_car.goto(300, y)
            a_car.setheading(180)
            self.all_cars.append(a_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(10)

    def increase_speed(self):
        self.car_speed *= 0.8







