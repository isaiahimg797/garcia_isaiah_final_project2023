# This code was created by Isaiah Garcia
# Sources:
    # Chris Cozort
    # https://www.dvlv.co.uk/pages/the-tkinter-cookbook.html
    # https://www.geeksforgeeks.org/python-gui-tkinter/
    # https://www.geeksforgeeks.org/reading-writing-text-files-python/

# Goals:
    # Create an app to track workouts
    # track sets and reps
    # option to add warmup sets
    # be able to view past workouts

from tkinter import *
import tkinter as tk
from setting import *
from datetime import datetime
import os

win = tk.Tk()
file = open(r"C:\Users\Isaiah.Garcia25\OneDrive - Bellarmine College Preparatory\Desktop\Computer Programming\Code\garcia_isaiah_final_project2023\garcia_isaiah_final_project2023\saves.txt", "a+")

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
    # variable which can be changed by the set command
    global clicked
    clicked = StringVar()
    # sets the intial string in the dropdown menu
    clicked.set("Select an Exercise")  
    # expand the list in the dropdown menu
    drop = OptionMenu(f2 , clicked , *excercises) 
    # place the drop down menu
    drop.grid(row=1, column=1, padx=5)
    # create a list of all labels - theres none unitl the function runs
    # when add button is pressed, log the name of excercise, # of reps, etc
    def create_label():
        # find number of labels
        global count
        count = len(labels) +1
        # create a label with the string chosen from a list
        global current_label
        current_label = tk.Label(f2, text= " ")
        # place the label
        current_label.grid(row=2 + 2*count, column=1)
        # add the new label to the list of labels
        labels.append(current_label)
        # place the label
        current_label.grid(row=2 + 2*count, column=1)
        # set what the label text is
        current_label.config(text = clicked.get())
        # shorten these labels because they will be used a lot
        reps_label = tk.Label(f2, text= "Reps")
        weight_label = tk.Label(f2, text= "Weight")
        # create entry boxes to enter the # of reps and sets
        global reps
        global weight
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
    dt_string = datetime.now().strftime("%m/%d/%Y %H:%M") 
    file.writelines(f"Time: {dt_string}, Set: {str(count)}, {current_label.cget('text')}, Reps: {reps.get()}, Lbs: {weight.get()} \n")
    file.flush()
    os.fsync(file.fileno())

def read():
    file.readlines()
    print(file.readlines())

# on the first page, create a button to log a workout
f1 = tk.Frame(win)
log_button = tk.Button(f1, text="Log Workout", command=showf2)
log_button.grid()
f1.pack()
view_button = tk.Button(f1, text="View Past Workout", command=read)
view_button.grid()

# setup page two
f2 = tk.Frame(win)
add()
return_button= tk.Button(f2, text="Menu", command=showf1)
return_button.grid(row=1, column=4, padx=5)
done_button = tk.Button(f2, text="Save", command=save)
done_button.grid(row= 1, column=3, padx=5)

win.mainloop()
