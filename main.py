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
    clicked.set("Select an Exercise")  
    drop = OptionMenu(f2 , clicked , *excercises) 
    drop.pack(side=LEFT) 
    labels = []
    def create_label():
        count = len(f2.winfo_children())
        label = tk.Label(f2, text= " ")
        label.pack()
        labels.append(label)
        label.pack(side=TOP)
        label.config( text = clicked.get() )
        reps = tk.Entry(f2).pack(side= LEFT)
        sets = tk.Entry(f2).pack(side= LEFT)
    log_button = tk.Button(f2, text="Add", command=create_label)
    log_button.pack(side=LEFT)
    

# on the first page, create a button to log a workout
f1 = tk.Frame(win)
log_button = tk.Button(f1, text="Log Workout", command=showf2, font=('Helvetica bold', 20))
log_button.pack()
f1.pack()

# setup page two
f2 = tk.Frame(win)
add()

win.mainloop()
