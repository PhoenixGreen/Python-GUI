from tkinter import *

#Main window & Background image - Tkinter:
window = Tk()
window.title("Background Image and lables")

images = PhotoImage(file = "trees1.gif").subsample(3, 3)
my_image = Label(window, image = images)
my_image.grid(row = 0, column = 0, columnspan = 3)


# Create Label Left
label_left = Label(window, text = "Label - Left", font = ("Helvetica", 16), fg = "black")
label_left.grid(row = 1, column = 0)

# Create Label Middle
label_bottom = Label(window, text = "Label - Middle", font = ("Helvetica", 24), fg = "red")
label_bottom.grid(row = 1, column = 1)

# Create Label Right
label_right = Label(window, text = "Label - Right", font = ("Helvetica", 16), fg = "black")
label_right.grid(row = 1, column = 2)


# Start the program
mainloop()
