from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("red")
        self.penup()
        self.cor_x = 10
        self.cor_y = 10

    def move_ball(self):
        new_x = self.xcor() + self.cor_x
        new_y = self.ycor() + self.cor_y
        # print(new_x, new_y)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.cor_y *= -1
        # print(self.cor_y)

    def bounce_x(self):
        self.cor_x *= -1
        # print(self.cor_x)

    def again(self):
        self.goto(x=0, y=0)
        self.bounce_x()




