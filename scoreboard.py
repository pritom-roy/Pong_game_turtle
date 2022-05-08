from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.goto(x=-200, y=270)
        self.write(f"Left_hand: {self.left_score}", align="center", font=("Verdana", 14, "normal"))
        self.goto(x=--200, y=270)
        self.write(f"Right_hand: {self.right_score}", align="center", font=("Verdana", 14, "normal"))

    def add_score_left(self):
        self.left_score += 1
        self.clear()
        self.update()

    def add_score_right(self):
        self.right_score += 1
        self.clear()
        self.update()

    def game_win_left(self):
        self.goto(x=0, y=20)
        self.write("Left Hand Win", align="center", font=("Verdana", 16, "bold"))

    def game_win_right(self):
        self.goto(x=0, y=20)
        self.write("Right Hand Win", align="center", font=("Verdana", 16, "bold"))
