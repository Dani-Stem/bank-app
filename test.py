
import tkinter as tk
from tkinter import *

master = Tk()

def option_a():
    user_imput = "a"
    return user_imput

def option_b():
    user_imput = "b"
    return user_imput

Label(master, text='Welcome to The Dani Bank').grid(row=1)
Label(master, text='What would you like to do?').grid(row=2)
button = tk.Button(master, text='Create account', width=25, command=master.destroy).grid(row=3)
button = tk.Button(master, text='Access account', width=25, command=test).grid(row=3, column=1)
button = tk.Button(master, text='Exit', width=25, command=master.destroy).grid(row=3, column=2)
mainloop()
