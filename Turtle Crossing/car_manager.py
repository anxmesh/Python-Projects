# Importing the required libraries
import turtle as tt
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Defining the CarManager class
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Function to create a single car
    def crate_car(self):
        randome_chance = random.randint(1, 6)
        if randome_chance == 1:
            new_car = tt.Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # function to move the cars from one edge to another
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Function to increase the speed of the car
    def speed_update(self):
        self.car_speed += MOVE_INCREMENT




