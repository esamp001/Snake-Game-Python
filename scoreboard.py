from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("save_data.txt") as data:
            self.highest_score = int(data.read())
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("save_data.txt", mode="w") as data:
            data.write(f"{self.highest_score}")
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.write(arg=f"Score:{self.score}", align="center", font=("Arial", 18, "bold"))
        self.clear()
        self.update_scoreboard()




