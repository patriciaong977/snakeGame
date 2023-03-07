''' The main file for the snake game.'''
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)  # Turn off the screen updates.

# Initializing Classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
        snake.extend() # Add a new segment to the snake.
        # Add a new segment to the snake, Update the scoreboard.
        scoreboard.increase_score()

    # Detect collision with the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        GAME_IS_ON = False
        scoreboard.game_over()

    # Detect collision with the tail.
    for segment in snake.segments:
        '''If the head collides with any segment in the tail, the game ends. Trigger game over.'''
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            GAME_IS_ON = False
            scoreboard.game_over()




# Exit the Screen on Click
screen.exitonclick()
