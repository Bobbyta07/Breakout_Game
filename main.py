from turtle import Screen, Turtle
from random import random
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time

game_on = False
screen = Screen()
screen.title('Breakout Game')
screen.bgcolor('black')
screen.setup(width=1000, height=600)
screen.tracer(0)
paddle = Paddle()
ball = Ball()
# Create Breaks
bricks = Bricks()
# print(len(bricks.brick_ls))


screen.listen()
screen.onkey(key='Right', fun=paddle.move_right)
screen.onkey(key='Left', fun=paddle.move_left)

if paddle:
    game_on = True

while game_on:
    time.sleep(0.1)
    # move ball
    ball.move_ball()
    screen.update()

    # get ball to bounce
    if ball.ycor() > 275:
        ball.bounce_y()

    elif ball.xcor() > 475 or ball.xcor() < -475:
        ball.bounce_x()

    # detect collision with Paddle

    if ball.distance(paddle) < 90 and ball.ycor() < -255:
        ball.bounce_y()

    # detect collision with bricks
    for brick in bricks.brick_ls:
        if ball.distance(brick) < 50:
            brick.hideturtle()
            bricks.brick_ls.remove(brick)
            ball.bounce_y()

screen.exitonclick()
