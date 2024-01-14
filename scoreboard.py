from turtle import Turtle
ALIGNMET = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = self.read_high_score()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def save_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMET, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()