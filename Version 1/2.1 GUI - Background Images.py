from tkinter import *

#Main window & Background image - Tkinter:
window = Tk()
window.title("Background Image")

canvas = Canvas(bg = "black", height = 350, width = 600)
scene = PhotoImage(file = "trees1.gif").subsample(3, 3)
canvas.create_image(0, 0, image = scene, anchor = NW)
canvas.pack()


# Start the program
window.mainloop()
