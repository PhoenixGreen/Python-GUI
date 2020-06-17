from tkinter import *

#Main window & Background image - Tkinter:
window = Tk()
window.title("Background Image and lables")

canvas = Canvas(bg = "black", height = 350, width = 600)
scene = PhotoImage(file = "trees.gif").subsample(3, 3)
canvas.create_image(0, 0, image = scene, anchor = NW)
canvas.pack()


# Create Label Left
label_left = Label(window, text = "Label - Left", font = ("Helvetica", 16), fg = "black")
label_left.pack(side = LEFT)

# Create Label Right
label_right = Label(window, text = "Label - Right", font = ("Helvetica", 16), fg = "black")
label_right.pack(side = RIGHT)

# Create Label Middle
label_bottom = Label(window, text = "Label - Bottom", font = ("Helvetica", 24), fg = "red")
label_bottom.pack(side = BOTTOM)


# Start the program
mainloop()
