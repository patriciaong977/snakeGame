from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    '''Creating the Snake body, and Moving the Snake'''

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        '''S1: Create the snake body. Turtle = 20x20 pixels'''
        for pos in STARTING_POSITIONS:  # For each pos in the list.
            snake = Turtle("square")  # Create a square turtle.
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.segments.append(snake)

    def move(self):
        '''S2: Move the snake body'''
        # # 3,2,1 - Start at 3, stop at 1, step -1
        for seg_num in range(len(self.segments) - 1, 0, -1,):
            # new_x = self.segments[seg_num - 1].xcor()
            # new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.segments[0].forward(MOVE_DISTANCE)
