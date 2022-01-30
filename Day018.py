#Day018 
from re import S
from turtle import Turtle, Screen, circle, fd
import turtle
import random
jeff = Turtle()
turtle.colormode(255)
#jeff.pensize(5)
loopSize = 20
jeff.home()
""""
for x in range(25):
    jeff.pencolor([random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
    jeff.circle(1)
    jeff.up()
    jeff.fd(loopSize)
    jeff.down()
    jeff.pencolor([random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)])
    jeff.circle(1)
    jeff.left(90)
    jeff.up()
    jeff.fd(loopSize)
    jeff.down()
    loopSize += 10
"""

jeff.speed("fastest")
for x in range(720):
    jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    jeff.circle(1+x)
    jeff.rt(4)



"""""
jeff.speed("fastest")
for x in range(2500):
    direction = ["fd","bk","rt",'lt']
    move = random.choice(direction)
    if move == "fd":
        jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        jeff.fd(25)
    if move == "bk":
        jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        jeff.bk(25)
    if move == "rt":
        jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        jeff.rt(90)
        jeff.fd(25)
    if move == "lt":
        jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        jeff.lt(90)
        jeff.fd(25)




jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
for x in range(3):
    jeff.forward(100)
    jeff.right(120)
jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
for x in range(4):
    jeff.forward(100)
    jeff.right(90)
jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
for x in range(5):
    jeff.forward(100)
    jeff.right(72)
jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
for x in range(6):
    jeff.forward(100)
    jeff.right(60)  
jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
for x in range(8):
    jeff.forward(100)
    jeff.right(45)  
jeff.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
for x in range(10):
    jeff.forward(100)
    jeff.right(36)





def moveJeffInASquare():
    for x in range(4):
        jeff.pd
        jeff.forward(100)
        jeff.circle(5)
        jeff.pu
        jeff.left(90)
    





for x in range(9):
    jeff.pd()
    jeff.forward(25)
    jeff.pu()
    jeff.forward(25)
    jeff.shape("circle")
"""

screen = Screen()
screen.exitonclick()
