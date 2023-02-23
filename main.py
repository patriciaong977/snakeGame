from turtle import Screen, Turtle
from snake import Snake
import time

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)  # Turn off the screen updates.

snake = Snake()

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



# Exit the Screen on Click
screen.exitonclick()
