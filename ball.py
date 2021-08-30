from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()

    def move(self):
        self.setx(self.xcor() + 15)
        self.sety(self.ycor() + 10)
