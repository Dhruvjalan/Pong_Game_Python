from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("White")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, 0)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 60)
            print("UP")

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 60)
            print("Down")
