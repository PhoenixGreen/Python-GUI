from tkinter import *

image_list = [
    "trees1.gif", "image 1 description",
    "trees2.gif", "image 2 description",
]

current = 0

#Main window & Background image - Tkinter:
window = Tk()
window.title("Background Image and lables")


# Action After Button Press
def after_click():
    global current
    global images

    if current < len(image_list) -2:
        current = current +2
    else:
        current = 0

    # Next Image
    images = PhotoImage(file = image_list[current]).subsample(3, 3)
    my_image = Label(window, image = images)
    my_image.grid(row = 0, column = 0, columnspan = 3)

    # Next Text Description
    description = Label(window, text = image_list[current +1])
    description.grid(row = 1, column = 0, columnspan = 2)


# Create Button - Next Image
button_right = Button(window, text = "Next Image", width = 30, command = after_click)
button_right.grid(row = 1, column = 2)

# Start the program
mainloop()
