import turtle
from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0

        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 250)
        self.print_score()
    def print_score(self):

        self.write(arg= f"Score is {self.score}",move=False,align = ALIGNMENT,font = FONT)
    def score_up(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align = ALIGNMENT,font =FONT)