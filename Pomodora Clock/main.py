# ---------------------------- LIBRARIES ------------------------------- #
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e28f83"
GREEN = "#4a503d"
CREAM = "#faf2da"
OLIVE = "#8e9775"
FONT_NAME = "Courier"
reps = 0
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps=0
    window.after_cancel(timer)
    Timer_label.config(text="TIMER", fg=OLIVE)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    if reps % 2 ==1:
        count_down(work_sec)
        Timer_label.config(text="WORK", fg=OLIVE)
    elif reps == 8:
        Timer_label.config(text="BREAK", fg=PINK)
        count_down(long_break)
    else:
        Timer_label.config(text="BREAK", fg=GREEN)
        count_down(short_break)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(0, work_sessions):
            marks +="🔺"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Setting up the Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=CREAM)

# Setting up the Canvas
canvas = Canvas(width=200, height=224, bg=CREAM, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)

# Setting up the labels
Timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=OLIVE, bg=CREAM)
Timer_label.grid(column=2, row=0)

checkmark_label = Label(fg=OLIVE, bg=CREAM)
checkmark_label.grid(column=2,row=3)

# Setting up the buttons
start_button = Button(text="Start", command=start_timer, font=("Arial", 16, "normal"),
                      borderwidth=10, fg=PINK, bg=CREAM)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, font=("Arial", 16, "normal"),
                      borderwidth=10, bg=CREAM, fg=PINK)
reset_button.grid(column=3, row=2)

window.mainloop()
