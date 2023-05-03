# Used to popular colors list, deleted some lighter colors
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
          (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
          (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
          (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

from turtle import Turtle, Screen
import random
import turtle as turtle_module

hirst_the_turtle = Turtle()
hirst_the_turtle.shape("turtle")
hirst_the_turtle.penup()
turtle_module.colormode(255)
hirst_the_turtle.speed("fastest")
hirst_the_turtle.setposition(-250,-250)


for dots in range(1,101):
    hirst_the_turtle.dot(20, random.choice(colors))
    hirst_the_turtle.forward(50)
    if dots % 10 == 0:
        current_y_position = hirst_the_turtle.ycor()
        hirst_the_turtle.setposition(-250, current_y_position + 50)
    if dots == 100:
        hirst_the_turtle.hideturtle()

screen = Screen()
screen.exitonclick()