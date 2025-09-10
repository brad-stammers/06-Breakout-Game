###################################################################################################
#   100 Days of Code: The Complete Python Pro Bootcamp
#   Portfolio Assignment 06 - Breakout Game
###################################################################################################

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block import Block
import time

# initialise
game_over = False

#setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BREAKOUT")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()
blocks = Block()
blocks.create_blocks()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #handle bouncing off walls and paddle
    if ball.distance(paddle) < 30:
        ball.bounce_y()

    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    #check if missed paddle
    if ball.ycor() < -280:
        game_over = True
        ball.hideturtle()
        scoreboard.game_over()

    # check for block collision
    for block in blocks.all_blocks:
        if block.distance(ball) < 30:
            scoreboard.point()
            block.hideturtle()
            ball.bounce_y()
            blocks.all_blocks.remove(block)
            break


screen.exitonclick()