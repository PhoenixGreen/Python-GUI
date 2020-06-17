from tkinter import *

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

label = Label(upper_frame, text = "Hello This is a label", bg = "white")
label.place(relwidth = 1.0, relheight = 1.0)

# Starts the program
window.mainloop()

'''
# lower frame
lower_frame = Frame(window, bg  = "#80c1ff", bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

'''
