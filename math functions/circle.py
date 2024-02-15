from turtle import *

speed(1000)
hideturtle()
bgcolor('black')
for i in range(80):
    color('white')
    circle(i)
    color('white')
    circle(i*1.2)
    color('white')
    circle(i*1.5)
    color('white')
    circle(i*1.7)
    left(5)
    backward(5)

done()