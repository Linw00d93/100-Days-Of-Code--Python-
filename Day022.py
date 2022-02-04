#Pong
from turtle import *
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

net = Turtle()
net.pu()
net.color("black")
net.pencolor("white")
net.pen
net.shape("square")
net.goto(0,-600)
net.pd()
net.pensize(15)
net.lt(90)
while net.ycor() < 600:
    net.pencolor("black")
    net.pu()
    net.fd(40)
    net.pencolor("white")
    net.pd()
    net.fd(40)

leftScore = 0
leftPlayer = Turtle()
leftPlayer.goto(-150,250)
leftPlayer.color('white')
leftPlayer.pu()
leftPlayer.hideturtle()
leftPlayer.write(leftScore,True, align="center" ,font=("Arial", 32 , "normal"))

rightScore = 0
rightPlayer = Turtle()
rightPlayer.goto(150,250)
rightPlayer.color('white')
rightPlayer.pu()
rightPlayer.hideturtle()
rightPlayer.write(str(rightScore),True, align="center" ,font=("Arial", 32 , "normal"))


screen.update()
paddle = Turtle()



def sketchUP():
    jeff = Turtle()
    def move_fowards():
        jeff.fd(10)
        print("up upupupupu")
        print(jeff.position())
    def move_backwards():
        jeff.bk(10)
        print(jeff.position())
    def turnLeft():
        jeff.lt(10)
        print(jeff.position())
    def turnRight():
        jeff.rt(10)
        print(jeff.position())
    def clear():
        jeff.reset()
    screen.onkey(key="Up", fun=move_fowards)
    screen.onkey(key="Down", fun=move_backwards)
    screen.onkey(key="Left", fun=turnLeft)
    screen.onkey(key="Right", fun=turnRight)
    screen.onkey(key="c", fun=clear)
screen.listen()

sketchUP()
print("Done")
screen.exitonclick()
""""
screen 
paddles
paddles movment 
ball 
ball movement
collison wall 


to move in another direction or bounce just muiltple the speed of direction by -1 

"""