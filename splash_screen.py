from tkinter import *
import time
import tkvideo

root = Tk()
root.title('Loading...')
root.geometry('640x360')
my_label = Label(root)
my_label.pack()
player = tkvideo.tkvideo("media_files\loading_media.mp4", my_label, loop = 1, size = (640,360))
player.play()

def delwindow():
    root.destroy()

my_label.after(3000,delwindow)
root.mainloop()

