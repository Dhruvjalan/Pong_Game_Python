from turtle import Turtle
from random import randrange


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        # self.left(37)
        self.shape("circle")
        self.color("White")
        self.xinc= 10
        self.yinc= -10

    def move(self):
        self.goto(self.xcor()+self.xinc,self.ycor()+self.yinc)
    
    def hit_top(self):
        self.yinc = -10
        
    def hit_bottom(self):
        self.yinc = 10
        
    
    def hit_left(self):
        self.xinc=10
    def hit_right(self):   
        self.xinc=-10