# TODO: functionality for the bricks
from turtle import Turtle


class Blocks:
    def __init__(self):
        self.all_blocks = []

    def create_blocks(self):
        # Create blocks and add them to the list
        for i in range(5):  # example: create 5 rows of blocks
            for j in range(10):  # example: create 10 blocks in each row
                x = -350 + j * 80  # calculate x-coordinate based on block position
                y = 200 - i * 50  # calculate y-coordinate based on block position
                new_block = Turtle('square')
                new_block.penup()
                new_block.color('yellow')
                new_block.turtlesize(stretch_wid=1.5, stretch_len=2)
                new_block.speed("fastest")
                new_block.goto(x, y)
                self.all_blocks.append(new_block)
