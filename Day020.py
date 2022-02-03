#Day020
#SNAKE?
print("""   
   _____             _        
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
from Day021 import * 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
snakePositions = [(0,0),(-20,0),(-40,0)]
screen.title("Snake the old way")
screen.tracer(0)
bodyParts = []
food = Food()
score = 0
super 


class Snake(Turtle):
    for positions in snakePositions:
        new_piece = Turtle()
        new_piece.pu()
        new_piece.shape("square")
        new_piece.color("green")
        new_piece.goto(positions)
        bodyParts.append(new_piece)
    scoreboard = Turtle()
    scoreboard.color('white')
    scoreboard.pu()
    scoreboard.goto(0,400)
    scoreboard.hideturtle()
    gameIsPlaying = True
    while gameIsPlaying == True:
        screen.listen()
        def turnLeft():
            bodyParts[0].lt(90)
            #print(bodyParts[0].pos())
        def turnRight():
            bodyParts[0].rt(90)
            #print(bodyParts[0].pos())

        screen.onkey(key="Left", fun=turnLeft)
        screen.onkey(key="Right", fun=turnRight)
        screen.update()
        time.sleep(0.1)

        scoreboard.clear()
        scoreboard.write(str(score), align="center" ,font=("Arial", 12, "normal"))

        for bodyPartsNum in range(len(snakePositions)-1,0,-1):
            newX = bodyParts[bodyPartsNum -1].xcor()
            newY = bodyParts[bodyPartsNum -1].ycor()
            bodyParts[bodyPartsNum].goto(newX,newY)
        bodyParts[0].fd(10)
        #print(bodyParts[0].pos())
        head = bodyParts[0].pos()
        if head[0] >= 500 or  head[1] >= 500 or  head[0] <= -500 or  head[1] <= -500:
            gameIsPlaying = False
            print("game over")
            gameOver = Turtle()
            gameOver.color('green')
            gameOver.pu()
            gameOver.hideturtle()
            gameOver.write("GAME OVER",True, align="center" ,font=("Arial", 32 , "normal"))
            break
        #Day021 stuff also 
        bigHead = bodyParts[0]
        #print(bodyParts[0])
        if bigHead.distance(food) <15:
            new_piece = Turtle()
            new_piece.pu()
            new_piece.shape("square")
            new_piece.color("green")
            new_piece.goto(bodyParts[-1].pos())
            snakePositions.append(new_piece.pos())
            bodyParts.append(new_piece)
            randomLocationX = random.randint(-275,275)
            randomLocationY = random.randint(-275,275)
            food.goto(randomLocationX, randomLocationY)
            score = 1 + score
            #print("Your too close man")
        tail = bodyParts[-1]
        if bigHead.distance(tail) <14:
            gameIsPlaying = False
            print("game over")
            gameOver = Turtle()
            gameOver.color('green')
            gameOver.pu()
            gameOver.hideturtle()
            gameOver.write("GAME OVER",True, align="center" ,font=("Arial", 32 , "normal"))
            break 
    screen.exitonclick()