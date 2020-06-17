from tkinter import *

# List of questions and answers
text_list = [
    "Question 0", "Answer 0",
    "Question 1", "Answer 1",
    "Question 2", "Answer 2",
    "Question 3", "Answer 3",
]

current = 0

# The main app window
window = Tk()
window.title("Weather App")
window.geometry("600x500")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)

# upper frame
upper_frame = Frame(window, bg  = "#80c1ff", bd = 5)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

# Creates the label text placeholder
label = Label()

# Action After Button Press
def after_click():
    global current
    global label
    label.destroy()
    if current < len(text_list):
        label = Label(upper_frame, text = text_list[current], font = "Arial 20", fg = "blue")
        label.place(relwidth = 1.0, relheight = 1.0)
        current = current +1
    else:
        label = Label(upper_frame, text = "That's all folks!", font = "Arial 20", fg = "blue")
        label.place(relwidth = 1.0, relheight = 1.0)

        
# Create button
button = Button(window, text = "Click", width = 20, command = after_click)
button.place(relx = 0.5, rely = 0.7, relwidth = 0.75, relheight = 0.1, anchor = "n")

# Runs the after_click() function - First time only
after_click()

# Starts the program
window.mainloop()
