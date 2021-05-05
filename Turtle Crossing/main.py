# importing the required libraries
import time
import turtle as tt
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Constants
SCREEN_UPDATE = 0.1

# Screen setup for the game
screen = tt.Screen()
screen.setup(width=600, height=600)
screen.title(" Crossy road DeepFake")
screen.tracer(0)
screen.listen()

# Creating the instances of the required game elements (player, cars, scoreboard)
player = Player()
screen.onkey(player.move, "Up")
scoreboard = Scoreboard()
car = CarManager()

# Driver code to run the game
game_is_on = True
while game_is_on:
    time.sleep(SCREEN_UPDATE)
    screen.update()

    # Generating the cars on the screen
    car.crate_car()
    car.move_cars()

    # checking for when the Turtle Reaches the finish line
    if player.ycor() > 280:
        player.refresh()
        scoreboard.levelupdate()
        car.speed_update()


    # collision detection for cars
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()