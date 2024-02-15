import turtle
import turtle as t 
t.speed(100000)
pattern=0

s=turtle.Screen()
s.bgcolor('black')

for i in range(1000):
    for color in ['white','white','white']:
        t.color(color)
        t.forward(pattern)
        t.right(90)
        t.right(1)
        pattern+=1
    
turtle.done()