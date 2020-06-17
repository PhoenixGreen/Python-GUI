from tkinter import *

# The main app window
window = Tk()
window.title("My first window")
window.geometry("700x500")

# Creating a background image
background_image = PhotoImage(file = "tree1.gif")
background = Label(window, image = background_image)
background.place(relwidth = 1.0, relheight = 1.0)


# Starts the program
window.mainloop()


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
