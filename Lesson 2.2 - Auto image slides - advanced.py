from tkinter import *

# The main app window and background image
window = Tk()
window.title("My Slide Show")
window.geometry("600x500")

background_image = PhotoImage(file = "landscape.png")
background_label = Label(window, image = background_image)
background_label.place(relwidth = 1.0, relheight = 1.0)


# upper frame - and text label
upper_frame = Frame(window, bg  = "#80c1ff", bd = 5)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

label = Label(upper_frame, text = "Welcome to my photo album", bg = "white")
label.place(relwidth = 1.0, relheight = 1.0)


# lower frame - and image in lower frame
lower_frame = Frame(window, bg  = "#80c1ff", bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

def image_rotator():
    global current
    global images

    image_list = [
        "tree1.gif",
        "tree2.gif",
        "tree3.gif",
    ]

    images = PhotoImage(file = image_list[current]).subsample(2, 2)
    image_slide_show = Label(lower_frame, image = images)
    image_slide_show.place(relwidth = 1.0, relheight = 1.0)

    if current < len(image_list) -1:
        current = current +1
    else:
        current = 0

    image_slide_show.config(image = images)
    window.after(2000, image_rotator)


# Runs the image_rotator the first time
current = 0
image_rotator()

# Starts the program
window.mainloop()


