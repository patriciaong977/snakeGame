'''The Food for the Snake Game.'''
from turtle import Turtle
import random

class Food(Turtle):
    '''Create the Food for the Snake to eat.
    Use Turtle to create the food.'''
    def __init__(self):
        super().__init__()

        # Comes from the Turtle class.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 pixels
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        '''Move the food to a random location on the screen.'''
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
