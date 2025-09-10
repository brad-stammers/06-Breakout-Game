from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=7.0, stretch_wid=1.0)
        self.penup()
        self.goto(0, -270)

    def go_left(self):
        print("go left")
        new_x = self.xcor() - 20
        print(f"nex_x = {new_x}")
        if new_x > -350:
            self.goto(new_x, self.ycor())

    def go_right(self):
        print("go right")
        new_x = self.xcor() + 20
        if new_x < 350:
            self.goto(new_x, self.ycor())
