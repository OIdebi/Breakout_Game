import time
from turtle import Screen
from player_clar import Character
from bricks import Blocks
from ball import Ball
from win_lose import WinLose

broken_brick = 0
# Screen layout and colour
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")

# blocks
blocks = Blocks()
blocks.create_blocks()

# player/paddle
# player movement
player = Character()
screen.onkey(player.move_left, key="a")
screen.onkey(player.move_right, key="d")

# ball
ball = Ball()
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    ball.move()

    # Detect coalition with brick
    for block in blocks.all_blocks:
        if block.distance(ball) < 30:
            ball.block_bounce()
            block.is_visible = False
            block.goto(1000, 1000)
            broken_brick += 1
        elif broken_brick == 50:
            WinLose().game_won()
            game_is_on = False

    else:
        # Detect coalition with wall
        if ball.xcor() >= 380 or ball.xcor() <= -380:
            ball.wall_side_bounce()
        elif ball.ycor() >= 280:
            ball.wall_top_bounce()
        elif ball.distance(player) < 62 and ball.ycor() < -230:
            print(ball.distance(player))
            ball.wall_top_bounce()
        elif ball.ycor() < -300:
            WinLose().game_over()
            game_is_on = False


screen.exitonclick()
