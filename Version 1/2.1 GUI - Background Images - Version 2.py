from tkinter import *

#Main window & Background image - Tkinter:
window = Tk()
window.title("Background Image")

images = PhotoImage(file = "trees1.gif").subsample(3, 3)
my_image = Label(window, image = images)
my_image.grid(row = 0, column = 0, columnspan = 3)


# Start the program
window.mainloop()
