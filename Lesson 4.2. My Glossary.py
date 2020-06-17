from tkinter import *

# The Main Window
window = Tk()
window.title("My Glossary")
window.geometry("400x500")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)

# The dictionary:
my_glossary = {
    "algorithm" : "Step by step instructions to perform a task the computer understands",
    "bug" : "A piece of code that causes the program to fail",
    }

# Button Press Function
def click_answer():
    entered_text = entry.get()
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word."

    label.config(text = definition)

# Create Text_Entry Box
entry = Entry(window, width = 20, bg = "light green" )
entry.place(relx = 0.5, rely = 0.09, relwidth = 0.7, relheight = 0.1, anchor = "n")

# Create Submit button
button = Button(window, text = "Submit", width = 10, command = click_answer)
button.place(relx = 0.5, rely = 0.2, relwidth = 0.7, relheight = 0.1, anchor = "n")

# Create Label
label = Label(window, text = "Enter a definition", bg = "light green", wraplength = 200)
label.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.3, anchor = "n")

# Run the main loop
window.mainloop()

