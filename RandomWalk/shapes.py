import random
from turtle import Turtle, Screen
tim = Turtle()
tim.speed(3)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink"]
def draw_shape(num_side):
    for i in range(num_side):
        tim.forward(100)
        tim.right(360 /num_side)

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
    tim.color(random.choice(colors))







