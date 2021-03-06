from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_edge()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.restart()
        score.left_scores()

    if ball.xcor() < -380:
        ball.restart()
        score.right_scores()

    ball.move()


screen.exitonclick()