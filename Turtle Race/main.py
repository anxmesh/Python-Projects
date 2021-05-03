import turtle as tt
import random
from turtle import _Screen

colors = ["red", "yellow", "orange", "green", "blue", "purple"]
ypos = [-75, -45, -15, 15, 45 ,75]
is_race_on = False
all_turtles = []

screen = tt.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? ENter a colour:")

if user_bet:
    is_race_on = True

for tindex in range(6):
    new_turtle = tt.Turtle(shape="turtle")
    new_turtle.color(colors[tindex])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=ypos[tindex])
    all_turtles.append(new_turtle)


while is_race_on:
    for turtlet in all_turtles:
        if turtlet.xcor() > 230:
            is_race_on = False
            winning_color = turtlet.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning colour was {winning_color}!")
            else:
                print(f"yYou've lost! The winning colour was {winning_color}!")
        randomdist = random.randint(0, 10)
        turtlet.forward(randomdist)



screen.exitonclick()