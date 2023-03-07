'''The Scoreboard for the Snake Game.'''
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    '''Create the Scoreboard for the Snake Game.'''
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        ''' Update the scoreboard when the snake eats a food.'''
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        ''' Write Game Over on the screen.'''
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        '''Increase and update the score.'''
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
