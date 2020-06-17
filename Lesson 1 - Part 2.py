from tkinter import *

# The main app window
window = Tk()
window.title("Frame for my app")
window.geometry("600x500")

# Background Image
background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)


# upper frame
upper_frame = Frame(window, bg = "#80c1ff", bd = 5)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

# lower frame
lower_frame = Frame(window, bg  = "#80c1ff", bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

# Starts the program
window.mainloop()





'''
Other arguments that can be used in the Label() function:

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


'''
Other .place()arguments that can be used:

anchor = N, − The exact spot of widget other options refer to: may be N, E, S, W, NE, NW, SE, or SW, compass directions indicating the corners and sides of widget; default is NW (the upper left corner of widget)
bordermode = INSIDE, (the default) to indicate that other options refer to the parent's inside (ignoring the parent's border); OUTSIDE otherwise.

height = 10, - Height in pixels.
width = 10, − Width in pixels.

relheight = 0.1, - Height as a float between 0.0 and 1.0, as a fraction of the height of the parent window.
relwidth = 1.0, − Width as a float between 0.0 and 1.0, as a fraction of the width of the parent window.

relx = 0.1, − Horizontal offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent window.
rely = 1.0, − Vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent window.

x = 1, − Horizontal offset in pixels.
y = 1, − Vertical offset in pixels.

'''
