from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.change_in_x = 10
        self.change_in_y = 10

    def move(self):
        self.setx(self.xcor() + self.change_in_x)
        self.sety(self.ycor() + self.change_in_y)

    def bounce_edge(self):
        self.change_in_y *= -1

    def bounce_paddle(self):
        self.change_in_x *= -1

    def restart(self):
        self.goto(0, 0)
        self.bounce_paddle()




