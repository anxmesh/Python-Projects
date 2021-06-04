# Quizzler: The Quiz Game 🔍
Welcome to Quizzler, an interactive Quiz game desinged in Pythin using the tkinter module and 
<a href="https://opentdb.com"> Open Trivia Database</a>.
## How it Works ⚙️
The game extracts questions from the Open Trivia Database and displays them on the screen. All questions are of the 
True or False variety. The user can then click on the appropriate button to signify their response, and the screen 
flashes green if they were correct, and red otherwise, before proceeding onto the next question.
<br> Once you reach the end, the score is displayed. 
## Resources 📦
### data.py 💾
This file contains the extraction of the quiz questions. By default, 10 questions are extracted and the genre is random.
To modfiy these parameters, refer to the <a href="https://opentdb.com/api_config.php"> Open Trivia Database API</a>.
### ui.py 👾
Contains the setup for the UI of the game.
### Quiz_brain.py 🧠
contains the quiz functionality functions and the data linked to each rendition of the quiz.
### Images 📁
Contains the graphic elements for the game such as button images.
