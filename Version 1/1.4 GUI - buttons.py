

from tkinter import *

# Building a tkinter window
window = Tk()
window.title("Simple Buttons")
window.geometry('640x640')


# After clicking the button
def after_click():
    my_label = Label(window, text = "I Clicked the button!")
    my_label.grid(row = 1, column = 0)

# Create button
my_button = Button(window, text = "Click the button!!", command = after_click)
my_button.grid(row = 0, column = 0)


# Start the program - tkinter
window.mainloop()



'''
Other arguments that can be used in the Button() function:

window, - This assigns the label to an area
text = "My Text App", - Text for the label to dispay
font = "Helvetica 32", - Font name and size of font
fg = "red", - Forground colour
bg = "Black", - Background colour
bd = 2, - Border size, works in conjunction with the "relief" argument
relief = SUNKEN, - Border styles include - RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID
width = 52, - Width of the text box being displayed
height = 3, - Height of the text box being displayed
pady = 5, - Padding around the top and bottom of the text
padx = 5, - Padding around the left and right of the text
anchor = E, - Position of the text inside of the text box (Acts like a compase)
'''

'''
Other arguments that can be used in the .grid() function:

row = 0, - Row position of the element 0 is first or top row
column = 0, - Column position of the element 0 is first or left column
columnspan = 3, - How many columns the element will occupy
rowspan = 3, - How many rows the element will occupy
sticky = W + E - Pins the element to the screen, can be useful for covering the full width of the app screen

pady = 5, - Padding around the top and bottom of the grid
padx = 5, - Padding around the left and right of the grid
'''
