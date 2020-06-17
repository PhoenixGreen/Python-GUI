from tkinter import *

# The main app window
window = Tk()
window.title("Simple Quiz")
window.geometry("410x500")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)

# The dictionary:
my_glossary = {
    "algorithm" : "Step by step instructions to perform a task the computer understands",
    "bug" : "A piece of code that causes the program to fail",
    "binary number" : "A number represented in base 2",
    }

# Key Press Function
def click_answer():
    entered_text = entry.get()
    output.delete(0.0, END)
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word."
    output.insert(END, definition)

# main_frame
main_frame = Frame(window, bd = 5)
main_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.9, relheight = 0.8, anchor = "n")


# Create Label
label = Label(main_frame, text = "Enter the word you want defining")
label.grid(row = 0, column = 0, columnspan = 2, pady = 10)

# Create text entry box
entry = Entry(main_frame, width = 20, bg = "light green" )
entry.grid(row = 1, column = 0)

# Add a submit button
button = Button(main_frame, text = "Get Answer", width = 10, command = click_answer)
button.grid(row = 1, column = 1)

# Create another label
label = Label(main_frame, text = "\nDefinition:")
label.grid(row = 3, column = 0, columnspan = 2, pady = 10)

# Create text box
output = Text(main_frame, width = 50, height = 6, wrap = WORD, background = "light green")
output.grid(row = 4, column = 0, columnspan = 2)

# Run the main loop
window.mainloop()
