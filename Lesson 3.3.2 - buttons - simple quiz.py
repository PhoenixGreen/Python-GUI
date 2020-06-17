from tkinter import *

# List of questions and answers
text_list = [
    "Question 0", "Answer 0",
    "Question 1", "Answer 1",
]

current = 0

# The main app window
window = Tk()
window.title("Simple Quiz")
window.geometry("600x500")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)

# upper frame
upper_frame = Frame(window, bg  = "#80c1ff", bd = 5)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

label = Label(upper_frame, text = "Hello", font = "Arial 20", fg = "blue")
label.place(relwidth = 1.0, relheight = 1.0)

# Action After Button Press
def after_click():
    global current
    if current < len(text_list):
        label.config(text = text_list[current])
        current = current +1
    else:
        label.config(text = "That's all folks!")

# Create button
button = Button(window, text = "Click", width = 20, command = after_click)
button.place(relx = 0.5, rely = 0.7, relwidth = 0.75, relheight = 0.1, anchor = "n")

# Starts the program
window.mainloop()

