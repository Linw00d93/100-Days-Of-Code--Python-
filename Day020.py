#Day020
#SNAKE?
print("""   _____             _        
  / ____|           | |       
 | (___  _ __   __ _| | _____ 
  \___ \| '_ \ / _` | |/ / _ \
  ____) | | | | (_| |   <  __/
 |_____/|_| |_|\__,_|_|\_\___|""")
print("🐍")
import numbers
from turtle import *
import random
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
snakePositions = [(0,0),(-20,0),(-40,0)]
screen.title("Snake the old way")
screen.tracer(0)
bodyParts = []

for positions in snakePositions:
    new_piece = Turtle()
    new_piece.pu()
    new_piece.shape("square")
    new_piece.color("green")
    new_piece.goto(positions)
    bodyParts.append(new_piece)
 
gameIsPlaying = True
while gameIsPlaying == True:
    screen.listen()
    def turnLeft():
        bodyParts[0].lt(90)
        print(bodyParts[0].pos())
    def turnRight():
        bodyParts[0].rt(90)
        print(bodyParts[0].pos())

    screen.onkey(key="Left", fun=turnLeft)
    screen.onkey(key="Right", fun=turnRight)
    screen.update()
    time.sleep(0.1)

    for bodyPartsNum in range(len(snakePositions)-1,0,-1):
        newX = bodyParts[bodyPartsNum -1].xcor()
        newY = bodyParts[bodyPartsNum -1].ycor()
        bodyParts[bodyPartsNum].goto(newX,newY)
    bodyParts[0].fd(10)
    print(bodyParts[0].pos())
    head = bodyParts[0].pos()
    if head[0] >= 500 or  head[1] >= 500 or  head[0] <= -500 or  head[1] <= -500:
        gameIsPlaying = False
        print("it worked")
        break
    
screen.exitonclick()