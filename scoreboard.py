from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 23, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt", "r") as file:
            high_score = int(file.read())
        return high_score

    def write_high_score(self, high_score):
        with open("data.txt", "w") as file:
            file.write(f"{high_score}")