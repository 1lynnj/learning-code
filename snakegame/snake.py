from turtle import Turtle


# constant variables to maintain for snake class
MOVE_DISTANCE = 20
# these are headings
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270





class Snake(Turtle):
    
    def __init__(self):
        super().__init__()
        self.snake_bodyparts = []  # list of turtle objects that make up snake
        self.create_snake()  # creating all turtles
        self.snake_head = self.snake_bodyparts[0]  # defining the first turtle that all other turtles follow

    ####Creates snake and starting point for first 3 body parts
    def create_snake(self):
        x = 20
        for _ in range(3):
            self.snake_body = Turtle()
            self.snake_body.penup()
            self.snake_body.color("white")
            self.snake_body.shape("square")
            x -= 20
            self.snake_body.goto(x, 0)
            self.snake_bodyparts.append(self.snake_body)

    def add_bodypart(self):
        self.snake_body = Turtle()
        self.snake_body.penup()
        self.snake_body.color("white")
        self.snake_body.shape("square")
        self.snake_bodyparts.append(self.snake_body)

    def reset(self):
        for seg in self.snake_bodyparts:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.snake_bodyparts = []
        self.create_snake()
        self.snake_head = self.snake_bodyparts[0]

    def move(self):
        # for loop so snake body parts move together
        for snake_part in range(len(self.snake_bodyparts) - 1, 0, -1):
            # 3 lines of code to tell the last body part (line 3) to go to position of second to last body part.
            new_x = self.snake_bodyparts[snake_part - 1].xcor()
            new_y = self.snake_bodyparts[snake_part - 1].ycor()
            self.speed('fastest')
            self.snake_bodyparts[snake_part].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    # functions to prevent snake from being able to travel back over the direction it is going
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
