import turtle
colorlist=['black','darkgrey','grey','lightgrey']
t=turtle.Turtle()
turtle.setup(height=700,width=700)
t.speed(10)

t.pendown()
sides=2
t.speed(1000)
for i in range(360):
    t.forward(i*2/sides+i)
    t.left(360/sides+1.5)
    t.color(colorlist[i%3])
    t.hideturtle()
    t.pensize(2)
turtle.done()