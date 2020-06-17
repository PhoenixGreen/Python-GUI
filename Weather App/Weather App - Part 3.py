from tkinter import *

# The main app window
window = Tk()
window.title("Weather App")
canvas = Canvas(window, height = 500, width = 600)
canvas.pack()

background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1, relheight = 1)


# upper frame
upper_frame = Frame(window, bg  = "#80c1ff", bd = 5)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

# lower frame
lower_frame = Frame(window, bg  = "#80c1ff", bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

label = Label(lower_frame, text = "Hello This is a label", bg = "white")
label.place(relwidth = 1, relheight = 1)

# Starts the program
window.mainloop()
