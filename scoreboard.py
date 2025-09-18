from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.score = 0
        self.write(f"{self.score}", False, "center", ("Courier", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "center", ("Courier", 18, "normal"))

