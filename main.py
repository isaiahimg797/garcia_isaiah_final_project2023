# This code was created by Isaiah Garcia
# Sources:
    # Chris Cozort
    # https://www.dvlv.co.uk/pages/the-tkinter-cookbook.html
    # https://www.geeksforgeeks.org/python-gui-tkinter/

# Goals:
    # Create an app to track workouts
    # track sets and reps
    # option to add warmup sets
    # be able to view past workouts

from tkinter import *
import tkinter as tk

win = tk.Tk()
win.geometry("600x600")

# second page
def showf2():
    f1.pack_forget()
    f2.pack()

# first page
def showf1():
    f2.pack_forget()
    f1.pack()

# adding an excercise function
def add():
    # take the string stored in clicked and apply the it to the label
    def show(): 
        label.config( text = clicked.get() )
    # list of excercises
    excercises = [
        "Choose an Exercise", 
        "Barbell Bench Press",
        "Dumbell Bench Press",
        "Tricep Pushdown",
        "Lat Pulldown",
        "Low Row",
        "Dumbell Curls",
        "Prescher Curls",
        "Barbell Back Squat",
        "Leg Extensions",
        "Hamstring Curls",
        "Hack Squat"
    ]       
    clicked = StringVar()
    clicked.set("Choose an Exercise")  
    drop = OptionMenu(f2 , clicked , *excercises,) 
    drop.pack()  
    button = Button( f2 , text = "Add" , command = show).pack()
    label = Label( f2 , text = " ") 
    label.pack()

# on the first page, create a button to log a workout
f1 = tk.Frame(win)
log_button = tk.Button(f1, text="Log Workout", command=showf2)
log_button.pack()
f1.pack()

# setup page two
f2 = tk.Frame(win)

add()






win.mainloop()
