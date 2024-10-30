from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highest_score = 0
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.write(arg=f"Score:{self.score}", align="center", font=("Arial", 18, "bold"))
        self.clear()
        self.update_scoreboard()




