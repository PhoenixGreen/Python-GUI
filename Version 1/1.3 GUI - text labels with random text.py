from tkinter import *
from random import *

# List of text items for display
text_list = [
    "Text Item 0",
    "Text Item 1",
    "Text Item 2",
    "Text Item 3",
    ]

text_item = choice(text_list)

# Building a tkinter window
window = Tk()
window.title("Random Text Generator")
window.geometry('640x640')

# Create Label one
label_one = Label(window, text = text_item, font = ("Arial", 40), fg = "red")
label_one.grid(row = 0, column = 0, sticky = W)


# Start the program - tkinter
window.mainloop()
