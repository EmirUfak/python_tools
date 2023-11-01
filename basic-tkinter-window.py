import tkinter as tk
from tkinter import ttk
from tkinter import *

def hello():
    label2 = ttk.Label(frame, 
                    text='This is button command.',
                    font=("Arial", 20),
                    ) 
    label2.grid(row=3, column=0, padx=30, pady=(30,10))
    

window = tk.Tk()
window.title("Basic Window")
window.eval('tk::PlaceWindow . center') 

frame = ttk.Frame(window)
frame.grid(row=0, column=0, sticky="nsew")

label = ttk.Label(frame, 
                    text='Hello World',
                    font=("Arial", 20),
                    ) 
label.grid(row=0, column=0, padx=30, pady=(30,10))

entry = ttk.Entry(frame, font=("Arial", 20)) 
entry.grid(row=1, column=0, padx=30, pady=(0,10))

button = ttk.Button(frame,                        
                    text="Button",
                    command = hello,
                        ) 



button.grid(row=2, column=0, pady=(0,30))

window.mainloop()
