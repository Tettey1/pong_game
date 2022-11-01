import time
from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong Game')

screen.listen()
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
score = Scoreboard()
screen.tracer(0)

screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
ball = Ball()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()
