import tkinter as tk
from tkinter import filedialog, Text, constants
import os

root = tk.Tk()
root.title("Macro")  # title of window
root.iconbitmap("d:/Coded stuff/Macro/mircle.ico")
apps = []  # list

canvas = tk.Canvas(root, height=550, width=550, bg="#999")  # sets the canvas
canvas.grid()

frame = tk.Frame(root, bg="black")  # creates a frame inside the canvas
frame.place(relwidth=1, relheight=1)

if os.path.isfile("save.txt"):  # reads the save file
    with open("save.txt", "r") as f:
        applist = f.read()
        applist = applist.split(",")
        apps = [x for x in applist if x.strip()]  # gets rid of empty spaces


def destroylabel():  # deletes labels
    for label in frame.winfo_children():
        label.destroy()


def showlabels():  # shows selected apps on screen
    for app in apps:
        label = tk.Label(frame, text=app, bg="black", fg="green", pady=5)
        label.grid()


def addApp():
    destroylabel()
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Add Apps",
        filetypes=(("executables", "*.exe"), ("all files", "*.*")),
    )
    apps.append(filename)
    showlabels()


def startApps():  # starts all selected apps
    for app in apps:
        os.startfile(app)


def cleanhistory():  # resets selected apps
    apps.clear()
    destroylabel()


def refresh():
    destroylabel()
    showlabels()


showlabels()

pickApp = tk.Button(  # button nr.1
    root,
    text="Choose app",
    padx=10,
    pady=5,
    fg="#989",
    bg="black",
    command=addApp,
)


start = tk.Button(  # button nr.2
    root, text="Start", padx=10, pady=5, fg="#989", bg="black", command=startApps
)


cleanApps = tk.Button(  # button nr.3
    root,
    text="Clean Selection",
    padx=10,
    pady=5,
    fg="#989",
    bg="black",
    command=cleanhistory,
)


refresh = tk.Button(  # button nr.1
    root,
    text="Refresh",
    padx=10,
    pady=5,
    fg="#989",
    bg="black",
    command=refresh,
)


pickApp.grid(row=0, column=4, sticky="sw")
start.grid(row=0, column=1, sticky="sw")
cleanApps.grid(row=0, column=2, sticky="sw")
refresh.grid(row=0, column=3, sticky="sw")

root.mainloop()  # end of loop

with open("save.txt", "w+") as f:  # creates save file
    for app in apps:
        f.write(app + ",")
