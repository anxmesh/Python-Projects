# importing the required libraries
import turtle as tt

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Defining the Player Class
class Player(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.refresh()
        self.setheading(90)

    # Function to trigger movement based on keypress
    def move(self):
        self.fd(MOVE_DISTANCE)

    # Functoin to refreah the player's position
    def refresh(self):
        self.goto(STARTING_POSITION)
