# Importing required libraries
import turtle as tt
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Setup
screen = tt.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("🏓")
screen.tracer(0)

# Creating the required elements (Paddles, ball, scoreboard)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# moving the paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# Game functioning
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with wall & inducing the bounce mechanism
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddles & inducing bounce mechanism
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting if the right paddle has missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detecting if the left paddle has missed the ball
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()