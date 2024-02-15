from turtle import *

speed(1000)
hideturtle()
bgcolor('white')
for i in range(1000):
    color('black')
    circle(i)
    color('black')
    circle(i*1.2)
    color('black')
    circle(i*1.5)
    color('black')
    circle(i*1.7)
    left(5)
    backward(5)

done()