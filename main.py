''' The main file for the snake game.'''
from turtle import Screen
import time
from snake import Snake
from food import Food

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)  # Turn off the screen updates.

# Initializing Classes
snake = Snake()
food = Food()

# Move the snake with the arrow keys.
screen.listen()
screen.onkey(snake.m_up, "Up")
screen.onkey(snake.m_down, "Down")
screen.onkey(snake.m_left, "Left")
screen.onkey(snake.m_right, "Right")

GAME_IS_ON = True
while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # If the snake head collides with the food, refresh the food.
    if snake.head.distance(food) < 15: # Food is 10x10 px, add 5 to account for the snake.
        food.refresh()
        # Add a new segment to the snake.


# Exit the Screen on Click
screen.exitonclick()
