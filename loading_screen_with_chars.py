import tkinter as tk
from tkinter import *
import threading
import time

def loadloop():
    global left_load
    i=0
    x=1
    while True:
        if i==1:
            txt = '\\'
            i=2
        elif i==2:
            txt='---'
            i=3
        elif i==3:
            txt='/'
            i=4
        else:
            txt='|'
            i=1
        left_load.config(text=txt)
        time.sleep(0.1)
        x=x+1
root = tk.Tk()
root.geometry("400x400")
left_load = tk.Label(root,text='|',font=('Helvetica 14 bold'))
left_load.pack(side=tk.TOP,expand=True)
threading.Thread(target=loadloop,args=()).start()
root.mainloop()