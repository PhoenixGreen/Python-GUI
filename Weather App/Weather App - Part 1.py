from tkinter import *

# The main app window
window = Tk()
window.title("Weather App")
canvas = Canvas(window, height = 500, width = 600)
canvas.pack()

background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1, relheight = 1)





# Starts the program
window.mainloop()
