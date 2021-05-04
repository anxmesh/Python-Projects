# Importing the required libraries
import turtle as tt

# creating the Ball class
class Ball(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Function to make the ball move on the screen
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    # Function for bouncing on y axis
    def bounce_y(self):
        self.y_move *= -1

    # Function for bouncing on the x axis and increase the speed of the ball each time
    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    # Function to reset position and moving direction of ball
    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.x_move *= -1




