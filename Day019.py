#Day019
#Higher order functions 
from turtle import *
import random
screen = Screen()


def sketchUP():
    jeff = Turtle()
    def move_fowards():
        jeff.fd(10)
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


    screen.listen()
    screen.onkey(key="Up", fun=move_fowards)
    screen.onkey(key="Down", fun=move_backwards)
    screen.onkey(key="Left", fun=turnLeft)
    screen.onkey(key="Right", fun=turnRight)
    screen.onkey(key="c", fun=clear)

def turtleRace():
    pinkT = Turtle()
    pinkT.shape("turtle")
    pinkT.color("pink")
    pinkT.pu()
    pinkT.goto(-450,0)
    yellowT = Turtle ()
    yellowT.pu()
    yellowT.shape("turtle")
    yellowT.color("yellow")
    yellowT.goto(-450,20)
    redT = Turtle()
    redT.pu()
    redT.shape("turtle")
    redT.color("Red")
    redT.goto(-450,40)
    greenT = Turtle()
    greenT.pu()
    greenT.shape("turtle")
    greenT.color("green")
    greenT.goto(-450,60)

    speed = [1 ,2 ,3 ,4, 5 ]
    while greenT.position()[0] <= 450 and redT.position()[0] <= 450 and yellowT.position()[0] <= 450 and pinkT.position()[0] <= 450 : 
        move = random.choice(speed)
        greenT.fd(move)
        move = random.choice(speed)
        redT.fd(move)
        move = random.choice(speed)
        yellowT.fd(move)
        move = random.choice(speed)
        pinkT.fd(move)

    if greenT.position()[0] >= 450:
        print(f"Green Turtle Won with a score of {greenT.position()[0]}\n") 
    if redT.position()[0] >= 450 :
        print(f"Red Turtle Won with a score of {redT.position()[0]}\n") 
    if yellowT.position()[0] >= 450 :
        print(f"Yellow Turtle Won with a score of {yellowT.position()[0]}\n") 
    if pinkT.position()[0] >= 450 : 
        print(f"Pink Turtle Won with a score of {pinkT.position()[0]}\n") 
    print("If tie turtrle with Highest score won\n")

screen.exitonclick()