import math 
import turtle

def xt(t, scale):
    return scale *(16 * math.sin(t)**3)

def yt(t, scale):
    return scale * (13 * math.cos(t)-5 * math.cos(2 * t) -2 * math.cos(3 * t)-math.cos(4 * t))

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
t.pensize(2)
t.pencolor('red')
t.hideturtle()

try:
    for scale in range(1,16):
        t.penup()
        t.goto(xt(0,scale), yt(0,scale))
        t.pendown()
    for i in range(0,70):
        x= xt(i/10, scale)
        y= yt(i/10, scale)
        t.goto(x,y)
finally:
    turtle.done()