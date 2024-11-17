from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self,x):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()