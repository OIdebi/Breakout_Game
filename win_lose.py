from turtle import Turtle
FONT = ("Courier", 24, "normal")


class WinLose(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)

    def game_won(self):
        self.color("green")
        self.write(f"You Won!", align="center", font=FONT)

    def game_over(self):
        self.color("red")
        self.write(f"Game Over...", align="center", font=FONT)
