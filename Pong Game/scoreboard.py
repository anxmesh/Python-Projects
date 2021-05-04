# Importing the required libraries
import turtle as tt

# creating the Ball class
class Scoreboard(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Function to update scoreboard
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Function to give Left player a point
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Function to give right player a point
    def r_point(self):
            self.r_score += 1
            self.update_scoreboard()
