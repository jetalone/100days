from turtle import Turtle, Screen
import random
import turtle as t

tom = Turtle()
t.colormode(255)


facing = [0,90,180,270]
tom.speed("fastest")


def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    col = (r,g,b)
    return col


for x in range(360):
    tom.pencolor(randomcolor())
    tom.setheading(x)
    tom.circle(100)





screen = Screen()
screen.exitonclick()