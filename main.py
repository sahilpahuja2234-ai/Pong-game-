from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import GameScore
import time
s1 = Screen()
s1.bgcolor("black")
s1.setup(width=800, height=600)
s1.title("Pong")
s1.tracer(0)
t1 = Turtle()
b = Ball()
p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
g = GameScore()
p1.speed("fastest")
p2.speed("fastest")

s1.listen()
s1.onkey(p1.go_up, "Up")
s1.onkey(p1.go_down, "Down")
s1.onkey(p2.go_up, "w")
s1.onkey(p2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(b.accel)
    s1.update()
    b.movement()
    #detect collision with ball
    if b.ycor() > 285 or b.ycor() < -285:
        b.ybounce()
    # detect collision with paddle
    if b.distance(p1) < 50 and b.xcor() > 340 or b.distance(p2) < 50 and b.xcor() < -340:
        b.xbounce()
    #detect if ball  is missed p2
    if b.distance(p1) > 50 and b.xcor() > 380:
        g.increase_score_p1()
        b.rest_position()
    #setect if ball is missed by p1
    if b.distance(p2) > 50 and b.xcor() < -380:
        g.increase_score_p2()
        b.rest_position()
    #enter ending
    if g.p1_score == 2 or g.p2_score == 2:
        s1.clear()
        t1.penup()
        t1.goto(0, 0)
        t1.write("Game over", align="center", font=("Courier", 80, "normal"))
        game_is_on = False

s1.exitonclick()

