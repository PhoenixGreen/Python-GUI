from tkinter import *

# List of questions and answers
text_list = [
    "Question 0", "Answer 0",
    "Question 1", "Answer 1",
    "Question 2", "Answer 2",
    "Question 3", "Answer 3",
]

current = 0

# Building a tkinter window
window = Tk()
window.title("My Simple Quiz")
window.geometry('640x640')

# Labels
main_label = Label(window, text = "Press the button for Q&A", font = ("Arial", 20), fg = "green")
main_label.grid(row = 0, column = 0, sticky = N)

label = Label(window, text = "", font = ("Arial", 20), fg = "red")
label.grid(row = 1, column = 0, sticky = W)

# Action After Button Press
def after_click():
    global current
    global label
    label.destroy()
    label = Label(window, text = text_list[current], font = ("Arial", 20), fg = "blue")
    label.grid(row = 1, column = 0, sticky = W)
    current = current +1

# Create button
button = Button(window, text = "Click", width = 20, command = after_click)
button.grid(row = 2, column = 0, sticky = S)


# Start the program - tkinter
window.mainloop()
