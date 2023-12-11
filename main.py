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
    drop.grid(row=1, column=1)
    labels = []
    # when add button is pressed, log the name of excercise, # of reps, etc
    def create_label():
        count = len(f2.winfo_children())
        label = tk.Label(f2, text= " ")
        label.grid(row=2 + 2*count, column=1)
        labels.append(label)
        label.grid(row=2 + 2*count, column=1)
        label.config(text = clicked.get())
        reps_label = tk.Label(f2, text= "Reps")
        weight_label = tk.Label(f2, text= "Weight")
        reps = tk.Entry(f2, width=5)
        weight = tk.Entry(f2, width=5)
        reps_label.grid(row=2 + 2*count, column=2)
        weight_label.grid(row=2 + 2*count, column=3)
        reps.grid(row=3 + 2*count, column=2)
        weight.grid(row=3 + 2*count, column=3)
    log_button = tk.Button(f2, text="Add", command=create_label)
    log_button.grid(row=1, column=2)
    

# on the first page, create a button to log a workout
f1 = tk.Frame(win)
log_button = tk.Button(f1, text="Log Workout", command=showf2, font=('Helvetica bold', 20))
log_button.pack()
f1.pack()

# setup page two
f2 = tk.Frame(win)
add()

win.mainloop()
