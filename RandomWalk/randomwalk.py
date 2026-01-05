import random
from turtle import Turtle, Screen
tim = Turtle()
tim.pensize(10)
colors=["red", "blue", "magenta", "cyan", "orange", "purple", "darkgreen", "teal", "maroon", "navy", "olive", "brown", "crimson", "darkcyan", "indigo"]


angles=[0,90,180,270]
def direction():
    return random.choice(angles)

for i in range(1000):
    tim.color(random.choice(colors))
    tim.setheading(direction())
    tim.forward(50)