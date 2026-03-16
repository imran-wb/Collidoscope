import turtle
import random 
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("white")

t.width(2)
t.speed(0)

col = ('black','black','black')
h=random.randint(1,999)
n=random.randint(1,8)
u=random.randint(1,999)
t.penup()
t.hideturtle()

x = s.window_width()/2 - 40
y = s.window_height()/2 - 150

t.goto(x, y)

t.write(f"h = {h}  n = {n}  u = {u}", align="right", font=("Arial",11,"bold"))
t.goto(0,0)
t.showturtle()
t.pendown()

for i in range(8600):
    t.pencolor(col[i % 3])
    t.forward(i *4)
    t.right(u)
    t.pencolor(col[i % 2])
    t.forward(i *n)
    t.right(h)