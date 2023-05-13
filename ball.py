# TODO: Functionality of the ball
from turtle import Turtle
import random

r_l = [-1,1]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.goto(0, -200)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_side_bounce(self):
        self.x_move *= -1

    def wall_top_bounce(self):
        self.y_move *= -1

    def block_bounce(self):
        direction = random.choice(r_l)
        self.x_move *= direction
