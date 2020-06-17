from tkinter import *

image_list = [
    "trees1.gif", "image 1 description",
    "trees2.gif", "image 2 description",
    "trees3.gif", "image 3 description",
]

current = 0

#Main window & Background image - Tkinter:
window = Tk()
window.title("Background Image and lables")

canvas = Canvas(bg = "black", height = 350, width = 600)
scene = PhotoImage(file = image_list[current]).subsample(3, 3)
canvas.create_image(0, 0, image = scene, anchor = NW)
canvas.pack()

# Action After Button Press
def after_click():
    global scene
    global current
    global label_bottom
    current = current +2

    if current < len(image_list):
        scene = PhotoImage(file = image_list[current]).subsample(3, 3)
        canvas.create_image(0, 0, image = scene, anchor = NW)
        canvas.pack()
    
        label_bottom.destroy()
        label_bottom = Label(window, text = image_list[current +1], font = ("Helvetica", 24), fg = "red")
        label_bottom.pack(side = BOTTOM)
    else:
        current = 0
        scene = PhotoImage(file = image_list[current]).subsample(3, 3)
        canvas.create_image(0, 0, image = scene, anchor = NW)
        canvas.pack()
    
        label_bottom.destroy()
        label_bottom = Label(window, text = image_list[current +1], font = ("Helvetica", 24), fg = "red")
        label_bottom.pack(side = BOTTOM)
        

# Create Button Right - Next Image
button_right = Button(window, text = "Next Image", width = 35, command = after_click, font = ("Helvetica", 16), fg = "black")
button_right.pack(side = RIGHT)

# Create Label Middle - Text Description
label_bottom = Label(window, text = image_list[current +1], font = ("Helvetica", 24), fg = "red")
label_bottom.pack(side = BOTTOM)

# Start the program
mainloop()
