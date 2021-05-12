# Importing the libraries
from tkinter import *

#window and button functoin setup
def button_clicked():
    new_text = float(input.get())*1.60934
    label3.config(text=f"{new_text}")

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

#Labels
label1 = Label(text="Miles", font=("Arial", 16, "italic"))
label1.grid(column=2, row=0)
label1.config(padx=5, pady=5)

label2 = Label(text="Is equal to", font=("Arial", 16, "normal"))
label2.grid(column=0, row=1)
label2.config(padx=5, pady=5)

label3 = Label(text="0", font=("Arial", 16, "normal"))
label3.grid(column=1, row=1)
label3.config(padx=5, pady=5)

label4 = Label(text="Kilometres", font=("Arial", 16, "italic"))
label4.grid(column=2, row=1)
label4.config(padx=5, pady=5)

#Button
button = Button(text="Calculate", command=button_clicked, font=("Arial", 16, "bold"), borderwidth=10)
button.grid(column=1, row=2)

#Entry
input = Entry(width=20)
print(input.get())
input.grid(column=1, row=0)



window.mainloop()