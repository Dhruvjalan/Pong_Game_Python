from turtle import Turtle, Screen
import time
from random import randrange
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
play=True

for i in range(-300, 300, 40):
    div = Turtle()
    div.penup()
    div.shape("square")
    div.color("White")
    div.shapesize(stretch_wid=1, stretch_len=0.5)

    div.goto(0,i)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
r_score= Scoreboard(-20)
l_score= Scoreboard(20)





ball = Ball()




screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down, "Down")

while play:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor()>280:
        ball.hit_top()
        print("HIT TOP")
    elif ball.ycor()<-280:
        ball.hit_bottom()
        print("HIT BOTTOM")

    if ball.xcor() > 330 and (ball.ycor() - r_paddle.ycor())**2 < 2500:
        print("Touches r paddle")
        ball.hit_right()
    if ball.xcor()<-330 and (ball.ycor()-l_paddle.ycor())**2<2500:
        print("Touches l paddle")
        ball.hit_left()
        
    if ball.xcor() > 360:
        r_score.increase_score()
        ball.goto(0,0)
    
    if ball.xcor()< -360:
        l_score.increase_score()
        ball.goto(0,0)


     # if ball.distance(paddle)<=20:







screen.exitonclick()