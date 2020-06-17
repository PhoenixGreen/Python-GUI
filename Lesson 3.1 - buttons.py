from tkinter import *

# List of questions and answers
text_list = [
    "Text 1",
    "Text 2",
]

current = 0

# The main app window
window = Tk()
window.title("Simple Buttons")
window.geometry("600x500")

# Change this label by clicking button
label = Label(window, text = "Hello", font = "Arial 20", fg = "blue")
label.place(relwidth = 1.0, relheight = 1.0)

# Action After Button Press
def after_click():
    global current
    label.config(text = text_list[current])
    current = current +1

# Create button
button = Button(window, text = "Click", width = 20, command = after_click)
button.place(relx = 0.5, rely = 0.7, relwidth = 0.75, relheight = 0.1, anchor = "n")

# Starts the program
window.mainloop()

