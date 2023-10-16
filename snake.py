from turtle import Screen,Turtle
import random
import time
MOVE_DISTANCE = 20

UP = 90
DOWN =270
RIGHT = 0
LEFT = 180
class Snake():

    def __init__(self):
        self.turtle = []
        self.create_snake()
        self.head = self.turtle[0]


    def extend(self):
        self.add(self.turtle[-1].position())
    def add(self,position):
        self.turtle.append(Turtle("square"))
        self.turtle[-1].goto(position)
        self.turtle[-1].color("white")
        self.turtle[-1].penup()

    def create_snake(self):
        for i in range(0, 3):
            self.turtle.append(Turtle("square"))
            self.turtle[i].goto(0 - i * 20, 0)
            self.turtle[i].color("white")
            self.turtle[i].penup()

    def move(self):


        for seg_num in range( len(self.turtle) -1, 0 , -1):
            new_x = self.turtle[seg_num- 1].xcor()
            new_y = self.turtle[seg_num - 1].ycor()
            self.turtle[seg_num].goto(new_x, new_y)
        self.turtle[0].forward(MOVE_DISTANCE)


    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


