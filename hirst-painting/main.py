
####cologram code to get colors from actual hirst painting
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# # print(colors)
# colors_list = []
# # rgb1 = []
#
# # this is Angela's code. Not sure how the color.rgb.r works with the list that is created by the extraction code above.
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_list.append(new_color)

# my code below
# #this code works and is modeled from the colorgram code example
# # for i in range(len(colors)):
# #     color = colors[i]
# #     rgb = color.rgb
# #     red = rgb[0]
# #     red = rgb.r
# #     green = rgb[1]
# #     green = rgb.g
# #     blue = rgb[2]
# #     blue = rgb.b
# #     rgb1.append(red)
# #     rgb1.append(green)
# #     rgb1.append(blue)
# #     rgb1 = tuple(rgb1)
# #     colors_list.append(rgb1)
# #     rgb1 = []
#
# print(f"colors_list: {colors_list}")

#####cologram code ends here


from turtle import Turtle, Screen
import turtle
import random


dot = Turtle()
colors_list = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18),
               (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23),
               (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25),
               (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244),
               (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]

turtle.colormode(255)
dot.shape("circle")
dot.pensize(20)
dot.penup()

def draw_row():
    for _ in range(10):
        # print(dot.position())
        dot.color(random.choice(colors_list))
        dot.pendown()
        dot.forward(1)
        dot.penup()
        dot.forward(49)
        dot.penup()

def position_new_row():
    x = dot.xcor()
    y = dot.ycor()
    dot.goto(x - 500, y + 50)

def draw_last_row():
    for _ in range(9):
        # print(dot.position())
        dot.color(random.choice(colors_list))
        dot.pendown()
        dot.forward(1)
        dot.penup()
        dot.forward(49)
        dot.penup()

# starting point
dot.goto(-250, -250)
draw_row()

for i in range(9):
    position_new_row()
    # dot.goto(-250, -200)
    if i == 8:
        draw_last_row()
    else:
        draw_row()

screen = Screen()
# screen.screensize(700, 700)
screen.exitonclick()
