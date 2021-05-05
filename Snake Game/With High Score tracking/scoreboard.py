# importing the required libraries
import turtle as tt


# Constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# DEfining the Scoreboard class
class Scoreboard(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.speed("fastest")
        self.goto(0, 270)
        self.color("white")
        self.ht()
        self.scoreprint()

    # Method to update the score
    def scoreupdate(self):
        self.score+=1
        self.scoreprint()

    # Method to print the score onto the screen
    def scoreprint(self):
        self.clear()
        self.write(f'SCORE = {self.score} HIGH SCORE = {self.high_score}', align=ALIGNMENT, font=FONT)

    # Method to print highscore and reset game to start
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f'{self.high_score}')
        self.score = 0
    # Method to indicate that the game is over
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(" GAME OVER. ", align=ALIGNMENT, font=FONT)