from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "normal"))
