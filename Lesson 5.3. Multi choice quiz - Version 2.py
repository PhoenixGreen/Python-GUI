from tkinter import *

# The Main Window
window = Tk()
window.title("Multi Choice Quiz")
window.geometry("800x800")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)

# Quiz Questions
QandA = [
    "Question 1", "Q1 - Option A", "Q1 - Option B", "Q1 - Option C", "Q1 - Option D", "Correct Answer",
    "Question 2", "Q2 - Option A", "Q2 - Option B", "Q2 - Option C", "Q2 - Option D", "Correct Answer",
    "That's all folks!","","","","","",
    ]

current = 0

# Options after Pressed Function
def answer(option):
    global current
    global label
    
    if QandA[current + 5] == option:
        label.config(text = "Correct")
    else:
        label.config(text = "Wrong")
    
    current = current + 6
    window.after(1000,quiz)
    

# The quiz
def quiz():
    global current
    global label
    
    # Create Label
    label = Label(window, text = QandA[current], bg = "light green", wraplength = 200)
    label.place(relx = 0.5, rely = 0.4, relwidth = 0.7, relheight = 0.3, anchor = "n")

    # Create Options buttons
    buttonA = Button(window, text = QandA[current + 1], width = 10, command = lambda: answer("a"))
    buttonA.place(relx = 0.15, rely = 0.2, relwidth = 0.2, relheight = 0.1, anchor = "n")

    buttonB = Button(window, text = QandA[current + 2], width = 10, command = lambda: answer("b"))
    buttonB.place(relx = 0.38, rely = 0.2, relwidth = 0.2, relheight = 0.1, anchor = "n")

    buttonC = Button(window, text = QandA[current + 3], width = 10, command = lambda: answer("c"))
    buttonC.place(relx = 0.62, rely = 0.2, relwidth = 0.2, relheight = 0.1, anchor = "n")

    buttonD = Button(window, text = QandA[current + 4], width = 10, command = lambda: answer("d"))
    buttonD.place(relx = 0.85, rely = 0.2, relwidth = 0.2, relheight = 0.1, anchor = "n")

# Runs the quiz function for the first time
quiz()

# Run the main loop
window.mainloop()


