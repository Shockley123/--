#万花筒
import turtle
import random
t=turtle.Pen()
t.speed(0)
t.width(2)
a=t.heading()
turtle.bgcolor("black")
color=["red","green","yellow","orange","blue","white","purple","gray","lemon chiffon","salmon"]
for m in range(50):
    t.pencolor(random.choice(color))
    size=random.randint(10,40)
    x=random.randrange(size,turtle.window_width()//2)
    y=random.randrange(size,turtle.window_height()//2)
    #第一象限螺旋线
    t.penup()
    t.setpos(x,y)
    t.setheading(a)
    t.pendown()
    for n in range(size):
        t.forward(n*2)
        t.left(91)
    #第二象限螺旋线
    t.penup()
    t.setpos(-x,y)
    t.setheading(180-a)
    t.pendown()
    for n in range(size):
        t.forward(n*2)
        t.left(91)
    #第三象限螺旋线
    t.penup()
    t.setpos(-x,-y)
    t.setheading(a-180)
    t.pendown()
    for n in range(size):
        t.forward(n*2)
        t.left(91)
    #第四象限螺旋线
    t.penup()
    t.setpos(x,-y)
    t.setheading(360-a)
    t.pendown()
    for n in range(size):
        t.forward(n*2)
        t.left(91)
