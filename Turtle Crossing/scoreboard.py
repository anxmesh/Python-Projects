# Importing the required libraries
import turtle as tt

# Constants
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


# Defining the Scoreboard Class
class Scoreboard(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.speed("fastest")
        self.goto(-280, 270)
        self.penup()
        self.ht()
        self.levelprint()

    # Method to update the levels
    def levelupdate(self):
        self.level += 1
        self.levelprint()

    # Method to print the level onto the screen
    def levelprint(self):
        self.clear()
        self.write(f'Level = {self.level}', align=ALIGNMENT, font=FONT)

    # Method to indicate that the game is over
    def game_over(self):
        self.goto(-90, 0)
        self.write(" GAME OVER. ", align=ALIGNMENT, font=FONT)
