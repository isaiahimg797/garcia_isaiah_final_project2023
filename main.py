# This code was created by Isaiah Garcia
# Sources:
    # Chris Cozort
    #  Dvlv - https://www.dvlv.co.uk/pages/the-tkinter-cookbook.html
    # Sandeep Jain - Geeks for geeks - https://www.geeksforgeeks.org/python-gui-tkinter/
    #   https://www.geeksforgeeks.org/reading-writing-text-files-python/
    # https://www.programiz.com/python-programming/datetime/current-datetime

# Goals:
    # Create an app to track workouts
    # track sets and reps
    # option to add warmup sets
    # be able to view past workouts

# import libraries
from tkinter import *
import tkinter as tk
from lists import *
from datetime import datetime
import os

win = tk.Tk()
# opens the text file that the data will be stored in
# file = open(r"C:\Users\Isaiah.Garcia25\OneDrive - Bellarmine College Preparatory\Desktop\Computer Programming\Code\garcia_isaiah_final_project2023\garcia_isaiah_final_project2023\saves.txt", "a+")
file = open("saves", "a+")

# move to second page command
def showf2():
    f1.pack_forget()
    f2.pack()

# move to first page command
def showf1():
    f2.pack_forget()
    f1.pack()

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

        # shorten these labels to variables
        reps_label = tk.Label(f2, text= "Reps")
        weight_label = tk.Label(f2, text= "Weight")

        # create entry boxes to enter the # of reps and sets
        global reps
        global weight
        reps = tk.Spinbox(f2, width=5, from_=0, to=1000)
        weight = tk.Spinbox(f2, width=5, from_=0, to=1000, increment=5)

        # place the reps and sets labels and entry boxes
        reps_label.grid(row=2 + 2*count, column=2)
        weight_label.grid(row=2 + 2*count, column=3)
        reps.grid(row=3 + 2*count, column=2)
        weight.grid(row=3 + 2*count, column=3)

        # button to save the set to the text files
        global done_button
        done_button = tk.Button(f2, text="Save", command=save, bg="red", font="bold")
        done_button.grid(row= 3 + 2*count, column=1, padx=5)

    # create the add button, when clicked, run the function to create all the entry boxes, labels, etc
    log_button = tk.Button(f2, text="Add", command=create_label)
    # place the add button
    log_button.grid(row=1, column=2, padx=5)

def save():
    # format of the date and time string
    dt_string = datetime.now().strftime("%m/%d/%Y %H:%M") 
    # in the text file, write:
        # date and time
        # set number - from list of labels
        # reps - takes the input from the entry box
        # how much weight - also take the input from the entry box
    file.writelines(f"{dt_string}, Set: {str(count)}, {current_label.cget('text')}, Reps: {reps.get()}, Lbs: {weight.get()} \n")
    # update the text file
    file.flush()
    os.fsync(file.fileno())
    # close the text file
    file.close
    done_button.destroy()

# this doesn't work right now
def read():
    content=file.readlines()
    print(content)

# on the first page, create a button to log a workout
f1 = tk.Frame(win)
log_button = tk.Button(f1, text="Log Workout", command=showf2)
log_button.grid()
# load page 1
f1.pack()
# doesnt work right now
view_button = tk.Button(f1, text="View Past Workout", command=read)
view_button.grid()

# setup page two
f2 = tk.Frame(win)
# run the function to setup everything on the second page
add()
# this doesn't really have a use, but it just brings you back to page 1
return_button= tk.Button(f2, text="Exit", command=showf1)
return_button.grid(row=1, column=3, padx=5)

win.mainloop()