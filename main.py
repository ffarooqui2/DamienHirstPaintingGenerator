# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# list_of_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     list_of_colors.append((r, g, b))
#
# print(list_of_colors)
import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
pen = Turtle()
color_list = [(164, 71, 45), (203, 153, 107), (224, 210, 113), (67, 94, 137), (155, 57, 74), (136, 166, 194),
              (46, 32, 25), (192, 135, 151), (37, 45, 111), (69, 117, 57), (29, 29, 78), (206, 92, 64), (108, 42, 63),
              (142, 190, 162), (118, 40, 34), (91, 156, 85), (62, 37, 62), (165, 200, 209), (37, 56, 34),
              (164, 203, 187), (170, 108, 143), (220, 179, 166), (41, 77, 37), (174, 187, 212), (117, 118, 151),
              (151, 140, 73)]

turtle.colormode(255)


def draw_hirst(gap, side):
    for i in range(side):
        for j in range(side):
            pen.dot(20, random.choice(color_list))
            pen.forward(gap)
        pen.backward(gap * side)

        pen.right(90)
        pen.forward(gap)
        pen.left(90)


pen.up()
pen.hideturtle()
pen.speed("fastest")
pen.setposition(-225, 210)
pen.width(10)
draw_hirst(50, 10)

screen.exitonclick()
