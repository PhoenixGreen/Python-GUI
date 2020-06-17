from tkinter import *
import datetime

window = Tk()
window.title("Image Rotator")
window.geometry("600x500")

def image_rotator():
    # All variables need to be global for reuse
    global current
    global images

    # This is the list of images to choose from
    image_list = [
        "tree1.gif",
        "tree2.gif",
        "tree3.gif",
    ]

    # 1. Gets an image, 2. Creates a label for the image, 3. Displays the image
    # Note: image_list[current] - changes the image each time
    images = PhotoImage(file = image_list[current]).subsample(2, 2)
    image_label = Label(window)
    image_label.place(relwidth = 1.0, relheight = 1.0)

    # Updates to a new image and keeps the program in range
    if current < len(image_list) -1:
        current = current +1
    else:
        current = 0

    # 1. updates the image_label, image argument to display the
    # next image from the images veriable
    # 2. pauses the program in milli-secdonds before running the
    # image_rotator() function again
    image_label.config(image = images)
    window.after(2000, image_rotator)


# Runs the image_rotator the first time
current = 0
image_rotator()

# Runs the main program
window.mainloop()

