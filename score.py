from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.left = 0
        self.right = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-50, 220)
        self.write(self.left, align="center", font=("Courier", 60, "normal"))
        self.goto(50, 220)
        self.write(self.right, align="center", font=("Courier", 60, "normal"))

    def left_scores(self):
        self.left += 1
        self.write_score()

    def right_scores(self):
        self.right += 1
        self.write_score()
