from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.goto(0, 0)
        self.accel = 0.1
        self.x_move = 10
        self.y_move = 10
    def movement(self):
        a = self.xcor() + self.x_move
        b = self.ycor() + self.y_move
        self.goto(a, b)
    def ybounce(self):
        self.y_move *= -1
    def xbounce(self):
        self.x_move *= -1
        self.accel *= 0.9
    def rest_position(self):
        self.goto(0, 0)
        self.accel = 0.1
        self.xbounce()



            # Bounce off left and right
        # if self.xcor() >= 380 or self.xcor() <= -380:
        #     self.setheading(180 - self.heading())


