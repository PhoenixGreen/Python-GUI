from tkinter import *

# Building a tkinter window
window = Tk()
window.title("Calculator App")

# Calculation Box - for Answer
e = Entry(window, width = 20, borderwidth = 5, font = ("Helvetica", 20))
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)


# Add function - action happens after button is pressed
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)

def button_add():
    global num1
    num1 = int(e.get())
    e.delete(0, END)

def button_equal():
    num2 = int(e.get())
    e.delete(0, END)
    e.insert(0, num1 + num2)
    

# Define / Make the buttons
button_1 = Button(window, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(window, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(window, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(window, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(window, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(window, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(window, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(window, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(window, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(window, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_add = Button(window, text = "+", padx = 39, pady = 20, command = button_add)
button_equal = Button(window, text = "=", padx = 91, pady = 20, command = button_equal)
button_clear = Button(window, text = "clear", padx = 79, pady = 20, command = button_clear)


# Put the buttons on the screen
button_1.grid(row = "3", column = "0")
button_2.grid(row = "3", column = "1")
button_3.grid(row = "3", column = "2")

button_4.grid(row = "2", column = "0")
button_5.grid(row = "2", column = "1")
button_6.grid(row = "2", column = "2")

button_7.grid(row = "1", column = "0")
button_8.grid(row = "1", column = "1")
button_9.grid(row = "1", column = "2")

button_0.grid(row = "4", column = "0")

button_add.grid(row = "5", column = "0")
button_equal.grid(row = "5", column = "1", columnspan = 2)
button_clear.grid(row = "4", column = "1", columnspan = 2)

# Start the program - tkinter
window.mainloop()
