# turtle画笑脸
```python
import turtle
import random
```
这里主要导入了turtle和random两个模块。
```
t=turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
```
基本操作:
1. 第一行给turtle一支笔
2. 第二行定义了turtle速度最快
3. 隐藏turtle
4. 背景黑色
```python
def draw_smile(x,y):
    #绘制脸
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #绘制眼睛
    t.setpos(x+15,y+60)
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.setpos(x-15,y+60)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.width(10)
    t.pencolor("black")
    t.penup()
    t.setpos(x+25,y+40)
    t.pendown()
    t.setpos(x+10,y+20)
    t.setpos(x-10,y+20)
    t.setpos(x-25,y+40)
    t.width(1)
```
代码如下：
```python
#笑脸
import turtle
import random
t=turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
def draw_smile(x,y):
    #绘制脸
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #绘制眼睛
    t.setpos(x+15,y+60)
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.setpos(x-15,y+60)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.width(10)
    t.pencolor("black")
    t.penup()
    t.setpos(x+25,y+40)
    t.pendown()
    t.setpos(x+10,y+20)
    t.setpos(x-10,y+20)
    t.setpos(x-25,y+40)
    t.width(1)
for x in range(100):
    x=random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
    draw_smile(x,y)
```
