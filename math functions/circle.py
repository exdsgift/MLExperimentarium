from turtle import *

speed(1000)
hideturtle()
bgcolor('white')
for i in range(80):
    color('black')
    circle(i)
    color('darkgrey')
    circle(i*1.2)
    color('grey')
    circle(i*1.5)
    color('lightgrey')
    circle(i*1.7)
    left(5)
    backward(5)

done()