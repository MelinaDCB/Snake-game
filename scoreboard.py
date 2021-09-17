from turtle import Turtle

FONT = ("Arial", 14, "normal")
ALIGNMENT = "center"



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.score = 0
        with open("scoreboard.txt") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", False, align="center", font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scoreboard.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
