from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    ball.move()


screen.exitonclick()