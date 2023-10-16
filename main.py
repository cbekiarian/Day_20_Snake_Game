from turtle import Screen,Turtle
import random
import time
from Food import Food
from scoreboard import Scoreboard

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snako")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
score = Scoreboard()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key= "Left")
screen.onkey(fun =snake.right,key ="Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)< 15:
        snake.extend()
        food.refresh()
        score.score_up()

    for seg in snake.turtle[1:]:

        if snake.head.distance(seg)<10:
            game_is_on = False
            score.game_over()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() <-280 or snake.head.ycor() >280:
        game_is_on =False
        score.game_over()
screen.exitonclick()
