#Day021 
#Class inheritance 
from turtle import *
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.color("red")
        self.speed("fastest")
        randomLocationX = random.randint(-275,275)
        randomLocationY = random.randint(-275,275)
        self.goto(randomLocationX, randomLocationY)

 
    

"""

if snake.head.distance(food)<15: 



"""