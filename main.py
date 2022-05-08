from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

new_ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

game_is_on = True
ball_speed = 0.06561
while game_is_on:
    time.sleep(ball_speed)
    new_ball.move_ball()
    if new_ball.ycor() > 280 or new_ball.ycor() < -280:
        # print(new_ball.xcor(), new_ball.ycor())
        new_ball.bounce_y()
        ball_speed *= 0.9

    if new_ball.distance(right_paddle) < 50 and new_ball.xcor() > 320 or new_ball.distance(
            left_paddle) < 50 and new_ball.xcor() < -320:
        # print(new_ball.xcor(), new_ball.ycor())
        print(new_ball.distance(left_paddle))
        new_ball.bounce_x()
        ball_speed *= 0.9
    elif new_ball.xcor() > 380:
        score.add_score_left()
        new_ball.again()
        ball_speed = 0.1

    elif new_ball.xcor() < -380:
        score.add_score_right()
        new_ball.again()
        ball_speed = 0.1

    if score.left_score == 5:
        score.game_win_left()
        game_is_on = False
    elif score.right_score == 5:
        score.game_win_right()
        game_is_on = False

    screen.update()

screen.exitonclick()
