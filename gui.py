import azel

import tkinter
import threading
from tkinter import messagebox
import time

Ra = 18.628944
Dec = 38.809389
run = 0


root = tkinter.Tk()
root.geometry("700x300")
root.title("find locator")

ra_input = tkinter.Entry(root, font=("arial", 30))
ra_input.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
dec_input = tkinter.Entry(root, font=("arial", 30))
dec_input.grid(row=0, column=3, columnspan=1, padx=5, pady=5)

azout = tkinter.Label(root, font=("arial", 25))
azout.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
elout = tkinter.Label(root, font=("arial", 25))
elout.grid(row=3, column=4, columnspan=1, padx=5, pady=5)

def update():
    Az, El = azel.RaDec2AzEl(Ra, Dec)
    azout.configure(text=str(Az))
    elout.configure(text=str(El))
    elout.after(1000, update)

def find():
    global Ra,Dec,run
    Ra = int(ra_input.get())
    Dec = int(dec_input.get())
    Az, El = azel.RaDec2AzEl(Ra, Dec)
    azout.configure(text=str(Az))
    elout.configure(text=str(El))
    if(run==0):
        run=1
        threading.Thread(target=update()).start()
find_btn = tkinter.Button(root, font=("arial", 30), text="find", command=find)
find_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
