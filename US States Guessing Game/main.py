# Importing the required libraries
import turtle as tt
import pandas as pd

# Creating the screen
screen = tt.Screen()
screen.title(" U.S. States Game 🇺🇸 ")
image = "blank_states_img.gif"
screen.addshape(image)
screen.screensize(800,800)
tt.shape(image)
tt.color("black")


#initialising some variables
correct_answers = []
missed_states = []

# Reading the csv containing the correct answers + coordinates
states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()

# Driver code to run the program
while len(correct_answers) <50:
    # asking the user for inputs
    answer_state = screen.textinput(title=f"{len(correct_answers)} / 50 Correct",
                                    prompt=" What's another State?").title()
    # Exiting the game.
    if answer_state == "Exit":
        for guesses in all_states:
            if guesses not in correct_answers:
                missed_states.append(guesses)
        learn = pd.Series(missed_states)
        learn.to_csv("Learn_the_following_States.csv")
        break

    if answer_state in all_states:
        correct_answers.append(answer_state)
        writer = tt.Turtle()
        writer.penup()
        writer.ht()
        state_data = states[states.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)
