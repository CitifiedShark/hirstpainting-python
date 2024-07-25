import colorgram
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract('hirstimage.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = Turtle()
screen = Screen()

screen.colormode(255)
tim.speed("fast")
tim.penup()

color_list = [(115, 160, 192), (134, 46, 112), (103, 34, 79), (200, 121, 179), (163, 62, 43), (18, 25, 48), (122, 121, 127)]

for y in range(10):
    tim.setx(-300)
    tim.sety(-300 + (y * 60))
    for x in range(10):
        tim.forward(60)
        color = random.choice(color_list)
        tim.dot(30, color)

tim.hideturtle()
screen.exitonclick()