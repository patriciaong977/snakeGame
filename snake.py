'''The Snake Body, and Movement for the Snake Game.'''
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''Creating the Snake body, and Moving the Snake'''

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''S1: Create the snake body. Turtle = 20x20 pixels'''
        for pos in STARTING_POSITIONS:  # For each pos in the list.
            self.add_segment(pos)

    def add_segment(self, pos):
        '''Add a new segment to the snake body when the snake eats a food.'''
        snake = Turtle("square")  # Create a square turtle.
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.segments.append(snake)

    def extend(self):
        '''Add a new segment to the snake body when the snake eats a food.
        Get the position of the last segment in the snake body, and add a new segment to the snake body.'''
        self.add_segment(self.segments[-1].pos()) # In python, can write a negative index to count from the end of the list.

    def move(self):
        '''S2: Move the snake body'''
        # # 3,2,1 - Start at 3, stop at 1, step -1
        for seg_num in range(len(self.segments) - 1, 0, -1,):
            # new_x = self.segments[seg_num - 1].xcor()
            # new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def m_up(self):
        ''' Move the snake up. Bearing = 90 degrees
        If the snake is moving down, it can't move up.'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def m_down(self):
        ''' Move the snake down. Bearing = 270 degrees
        If the snake is moving up, it can't move down.'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def m_left(self):
        ''' Move the snake left. Bearing = 180 degrees
        If the snake is moving right, it can't move left.'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def m_right(self):
        ''' Move the snake right. Bearing = 0 degrees
        If the snake is moving left, it can't move right.'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
