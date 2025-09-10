from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scoreboard()
        self.goto(-400, 240)
        self.pendown()
        self.goto(400, 240)
        self.penup()


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 30, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"GAME OVER    Score: {self.score}", align="center", font=("Courier", 30, "normal"))

