from turtle import Turtle
class GameScore(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))
    def increase_score_p1(self):
        self.p1_score += 1
        self.update_score()
    def increase_score_p2(self):
        self.p2_score += 1
        self.update_score()
