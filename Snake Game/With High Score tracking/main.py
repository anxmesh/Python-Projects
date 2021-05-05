# importing the required libraries
import turtle as tt
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup for game
screen = tt.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Hiss Hiss")
screen.tracer(0)

# creating the snake & its food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Moving the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Functioning of the game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Keeping score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoreupdate()

    # Detecting collisions with the wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        scoreboard.scoreprint()

    # Detecting collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            scoreboard.scoreprint()











screen.exitonclick()
