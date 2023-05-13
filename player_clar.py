from turtle import Turtle
# TODO: Functionality of the paddle
MOVE_DISTANCE = 20


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed('fastest')
        self.goto(0, -250)

    def move_left(self):
        self.bk(MOVE_DISTANCE)

    def move_right(self):
        self.fd(MOVE_DISTANCE)
