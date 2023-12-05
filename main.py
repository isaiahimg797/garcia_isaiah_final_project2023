# This code was created by Isaiah Garcia
# Sources:
    # Chris Cozort
    # https://www.dvlv.co.uk/pages/the-tkinter-cookbook.html

# Goals:
    # Create an app to track workouts
    # track sets and reps
    # option to add warmup sets
    # be able to view past workouts

from tkinter import *
import tkinter as tk

win = tk.Tk()
win.geometry("600x600")

def log(): 
    new= Toplevel(win)
    new.geometry("600x600")
    new.title("New Window")

Button(win, text= "Log Workout", height= 5, width= 20, font= ('Helvetica 20 bold'), command= log).pack()


win.mainloop()

