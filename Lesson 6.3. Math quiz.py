from tkinter import *
import random

# The Main Window
window = Tk()
window.title("Math Quiz")
window.geometry("800x800")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)

current = 1
points = 0

def the_question():
    global question
    global answer
    question_type = ["+", "-", "*"]
    operation = random.choice(question_type)
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)

    question = str(number1) + " " + operation + " " + str(number2)
    answer = eval(str(number1) + operation + str(number2))
    

def the_answer(entry):
    global label
    global answer
    global current
    global points
    
    entered_text = int(entry.get())
    if entered_text == answer:
        label.config(text = "Correct!")
        points = points + 10
    else:
        label.config(text = "That is not the answer!")

    if current == 10:
        label.config(text = "That's all folks!")
    else:
        current = current + 1
        the_question()
        window.after(1000,the_quiz)
        

def the_quiz():
    global label
    global question

    # Enter Answer Box
    entry = Entry(window, width = 20, bg = "light green" )
    entry.place(relx = 0.5, rely = 0.19, relwidth = 0.7, relheight = 0.1, anchor = "n")

    # Submit Answer button
    button = Button(window, text = "Submit Answer", width = 10, command = lambda: the_answer(entry))
    button.place(relx = 0.5, rely = 0.3, relwidth = 0.7, relheight = 0.1, anchor = "n")

    # Question and Answer Box
    label = Label(window, text = question, bg = "light green", wraplength = 400, font = "Helvetica 36")
    label.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.2, anchor = "n")

    # Your Points
    points_label = Label(window, text = "Question " + str(current) + ": You have " + str(points) + " /100 points", bg = "gray", fg = "white")
    points_label.place(relx = 0.5, rely = 0.0, relwidth = 1.0, relheight = 0.05, anchor = "n")


# Run the_question and the_quiz for the first time
the_question()
the_quiz()

# Run the main loop
window.mainloop()


