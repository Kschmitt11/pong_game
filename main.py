from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
p1_score = Scoreboard((-200, 260))
p2_score = Scoreboard((200, 260))

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50 or
        ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 380:
        p1_score.increase_score()
        ball.reset_ball()

    if ball.xcor() < -380:
        p2_score.increase_score()
        ball.reset_ball()

    screen.update()


screen.exitonclick()