# importing the required libraries
import turtle as tt

# CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Defining the Snake Class
class Snake:
    parts_of_snake = []
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creates the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Function to add segment onto the snake
    def add_segment(self, position):
        new_segment = tt.Turtle("square")
        new_segment.color("brown")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Function to move the snake
    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    # Function to increase the size of the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Functions to trigger movement based on keypress
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

