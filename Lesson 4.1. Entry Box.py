from tkinter import *

# The Main Window
window = Tk()
window.title("Entry Box")
window.geometry("400x500")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)

# Button Press Function
def click_answer():
    entered_text = entry.get()
    label.config(text = "Hello " + entered_text + " it's nice to meet you")

# Create Text_Entry Box
entry = Entry(window, width = 20, bg = "light green" )
entry.place(relx = 0.5, rely = 0.09, relwidth = 0.7, relheight = 0.1, anchor = "n")

# Create Submit button
button = Button(window, text = "Submit", width = 10, command = click_answer)
button.place(relx = 0.5, rely = 0.2, relwidth = 0.7, relheight = 0.1, anchor = "n")

# Create Label
label = Label(window, text = "Hello, what's your name?", bg = "light green", wraplength = 200)
label.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.4, anchor = "n")

# Run the main loop
window.mainloop()

