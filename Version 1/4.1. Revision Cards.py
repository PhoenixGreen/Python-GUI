from tkinter import *

# Key Press Function

def click_answer():
    entered_text = entry.get()
    output.delete(0.0, END)
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word."
    output.insert(END, definition)

# Main Window
window = Tk()
window.title("My Glossary")

# Create Label
Label(window, text = "Enter the word you want defining").grid(row = 0, column = 0, sticky = W)

# Create text entry box
entry = Entry(window, width = 20, bg = "light green" )
entry.grid(row = 1, column = 0, sticky= W)

# Add a submit button
button = Button(window, text = "Get Answer", width = 10, command = click_answer)
button.grid(row = 2, column = 0, sticky = W)

# Create another label
label = Label(window, text = "\nDefinition:")
label.grid(row = 3, column = 0, sticky = W)

# Create text box
output = Text(window, width = 75, height = 6, wrap = WORD, background = "light green")
output.grid(row = 4, column = 0, columnspan = 2, sticky = W)

# The dictionary:
my_glossary = {
    "algorithm" : "Step by step instructions to perform a task the computer understands",
    "bug" : "A piece of code that causes the program to fail",
    "binary number" : "A number represented in base 2",
    }

# Run the main loop
window.mainloop()
