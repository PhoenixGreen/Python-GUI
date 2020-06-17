from tkinter import *
import datetime

window = Tk()
window.title("My Clock")
window.geometry("600x500")

time_label = Label(window)
time_label.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    time_label.config(text = time)
    window.after(1000, clock)

# Runs the clock the first time
clock()

# Runs the main program
window.mainloop()
