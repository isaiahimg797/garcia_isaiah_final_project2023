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
import pickle
from setting import *

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
    # variable which can be changed but the set command
    clicked = StringVar()
    # sets the intial string in the dropdown menu
    clicked.set("Select an Exercise")  
    # expand the list in the dropdown menu
    drop = OptionMenu(f2 , clicked , *excercises) 
    # place the drop down menu
    drop.grid(row=1, column=1, padx=5)
    # create a list of all labels - theres none unitl the function runs
    labels = []
    # when add button is pressed, log the name of excercise, # of reps, etc
    def create_label():
        # find number of labels
        count = len(f2.winfo_children())
        # create a label with the string chosen from a list
        label = tk.Label(f2, text= " ")
        # place the label
        label.grid(row=2 + 2*count, column=1)
        # add the new label to the list of labels
        labels.append(label)
        # place the label
        label.grid(row=2 + 2*count, column=1)
        # set what the label text is
        label.config(text = clicked.get())
        # shorten these labels because they will be used a lot
        reps_label = tk.Label(f2, text= "Reps")
        weight_label = tk.Label(f2, text= "Weight")
        # create entry boxes to enter the # of reps and sets
        reps = tk.Entry(f2, width=5)
        weight = tk.Entry(f2, width=5)
        # place the reps and sets labels and entry boxes
        reps_label.grid(row=2 + 2*count, column=2)
        weight_label.grid(row=2 + 2*count, column=3)
        reps.grid(row=3 + 2*count, column=2)
        weight.grid(row=3 + 2*count, column=3)
    # create the add button, when clicked, run the function to create all the entry boxes, labels, etc
    log_button = tk.Button(f2, text="Add", command=create_label)
    # place the add button
    log_button.grid(row=1, column=2, padx=5)

def save():

    pass

# on the first page, create a button to log a workout
f1 = tk.Frame(win)
log_button = tk.Button(f1, text="Log Workout", command=showf2)
log_button.grid()
f1.pack()

# setup page two
f2 = tk.Frame(win)
add()
return_button= tk.Button(f2, text="Menu", command=showf1)
return_button.grid(row=1, column=4, padx=5)
done_button = tk.Button(f2, text="Done", command=save)
done_button.grid(row= 1, column=3, padx=5)

win.mainloop()
