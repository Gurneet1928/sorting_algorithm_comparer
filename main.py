import datetime as dt
import tkinter as tk
from tkinter import ANCHOR, BOTH, CENTER, GROOVE, RAISED, RIDGE, ttk
import numpy as np
import sys
import sort_tech as st
import time
import customtkinter as ctk
from playsound import playsound
import winsound
from PIL import Image, ImageTk
import splash_screen
import gc
import tkvideo
#--------------------------------Musics/Themeing/Global Variables-----------------------------------

winsound.PlaySound('media_files\song.wav', winsound.SND_ALIAS | winsound.SND_ASYNC + winsound.SND_LOOP )
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

label_list=[]
time_data={}
sorted_array=[]
song_status=True

#--------------------------------Algo Dictionary-----------------------------------

ag = {1:"selection_sort",
2:"bubble_sort",
999:"insertion_sort",
3:"merge_sort",
4:"cocktail_sort",
5:"heap_sort",
6:"pigeon_hole_sort",
7:"gnome_sort",
8:"shell_sort",
9:"odd_even_sort",
10:"cycle_sort"
}

complexities = {1:"O(n*n)",
2:"O(n*n)",
3:"O(nlogn)",
4:"O(n*n)",
5:"O(nlogn)",
6:"O(n+2^k)",
7:"O(n*n)",
8:"O(n(logn)^2) [Variable]",
9:"O(n*n)",
10:"O(n*n)"
}

#--------------------------------Main Window Creation-----------------------------------

root = ctk.CTk()
root.geometry("750x700")
root.title("Sorting Algorithm Comparer")

#-------------------------------------HEADING---------------------------------


ctk.CTkLabel(root,text="Sorting Algorithm Comparer",text_font=("Roboto Medium", 22,'underline')).pack(side=tk.TOP)


#-------------------------------------Music Player Controls---------------------------------

def change_song_status():
    global song_status
    if not song_status:
        volume_button.config(image=volume_unmute)
        winsound.PlaySound('media_files\song.wav', winsound.SND_ALIAS | winsound.SND_ASYNC + winsound.SND_LOOP)
        song_status=True
    else:
        volume_button.config(image=volume_mute)
        winsound.PlaySound(None, winsound.SND_PURGE)
        song_status=False

volume_mute = Image.open('media_files\song_mute.png')
resize_img = volume_mute.resize((40, 40))
volume_mute = ImageTk.PhotoImage(resize_img)
volume_unmute = Image.open('media_files\song_unmute.png')
resize_img = volume_unmute.resize((40, 40))
volume_unmute = ImageTk.PhotoImage(resize_img)
volume_button = tk.Button(root,image=volume_unmute,command=change_song_status)
volume_button.pack(anchor='ne',side=tk.TOP)


#-------------------------------------Notebook Tabs---------------------------------

'''customed_style = ttk.Style()
customed_style.configure('Custom.TNotebook.Tab', padding=[75, 5], font=('Helvetica', 10))'''
style = ttk.Style()
 
style.theme_create('pastel', settings={
    ".": {
        "configure": {
            "background": '#ffffcc', # All except tabs
            "font": 'red'
        }
    },
    "TNotebook": {
        "configure": {
            "background":'#8cb791', # Your margin color
            "tabmargins": [0, 0, 0, 0], # margins: left, top, right, separator
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": '#fbaf00', # tab color when not selected
            "padding": [85, 5], # [space between text and horizontal tab-button border, space between text and vertical tab_button border]
            "font":('Helvetica', 12)

        },
        "map": {
            "background": [("selected", '#bdff00')], # Tab color when selected
            "expand": [("selected", [1, 1, 1, 0])] # text margins
            
        }
    }
})
style.theme_use('pastel')
notebook = ttk.Notebook(root)

def exit_code():
    root.destroy()
    gc.collect()

mainframe = ctk.CTkFrame(notebook,width=700,height = 600,border_color='green',border_width=3)
mainframe.pack(fill='both',expand=True)
notebook.add(mainframe,text="MAIN MENU")
aboutframe = ctk.CTkFrame(notebook,width=700,height = 600,border_color='yellow',border_width=3)
aboutframe.pack(fill='both',expand=True)
notebook.add(aboutframe,text="ABOUT THE PROGRAM")
exit_button = ctk.CTkButton(notebook,text="CLICK HERE TO EXIT",command=exit_code,width=700,height = 600,border_color='blue',border_width=3,hover=False,text_font=("Verdana", 25))
exit_button.pack(fill='both',expand=True)
notebook.add(exit_button,text="EXIT THE PROGRAM")
notebook.pack(pady=(20,10),expand=True,fill=BOTH)


#-------------------------------------MainFrame Tab  => Data Row---------------------------------

def findbest():
    min_key = min(time_data, key=time_data.get)
    time.sleep(1)
    for i in range(0,3):
        min_key = min(time_data, key=time_data.get)
    ans = ag[min_key]
    txt = "Best Algorithm as per given data is : " + ans
    ans_label['text']=txt
    gc.collect()

def showsorted():
    global sorted_array
    sorted_data_text.delete(1.0,"end")
    sorted_data_text.insert(1.0,sorted_array)

def printdata():
    label_list.clear()
    time_data.clear()
    gc.collect()
    data_from_form = data_form.get('1.0', 'end')
    data_from_form = data_from_form.split()
    if not any(char.isalpha() for string in data_from_form for char in string):
        global sorted_array
        sorted_array = list(map(int, data_from_form))
        n=len(sorted_array)
        for i in range(n):
            for j in range(0, n-i-1):
                if sorted_array[j] > sorted_array[j+1]:
                    sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]
        vec_data = np.array(data_from_form)
        for i in range(1,11):
            global str
            fun = getattr(st,ag[i])
            val = fun(vec_data)
            val = "%.4f" %val
            time_data[i]=val
            fun_data = val + ' ms'
            label_list.append(ctk.CTkLabel(mainframe,text=fun_data))
            label_list[i-1].grid(row=i+i+1,column=3)
        findbest()
        showsorted()
    else:
        txt = 'Character(s) Found in Data !! Please try again'
        ans_label['text'] = txt
        

enterData_label = ctk.CTkLabel(mainframe,text="Enter the Data to be Sorted Here --> \n[ Use blank to seperate them ]").grid(row=0,column=0,padx=15)
data_form = tk.Text(mainframe,height=5,width=35, bg = "#264653",fg="white",bd=7,wrap="word")
vsb = ttk.Scrollbar(mainframe, command=data_form.yview, orient="vertical")
data_form.configure(yscrollcommand=vsb.set)
vsb.grid(row=0, column=2, sticky="ns")
data_form.grid(row=0,column=1, sticky="nsew",padx=(10,0),pady=(10,10))
sub_button = ctk.CTkButton(mainframe,text="<< SUBMIT DATA >>",command=printdata).grid(row=0,column=3,padx=10)

ans_label = tk.Label(mainframe,text='Comparison Result will be displayed here!!',font=("Cambria", 17),relief=GROOVE,justify=CENTER,background='#292929',fg='white')
ans_label.grid(row=25,column=0,columnspan=4,padx=(10,0))

hsb = ttk.Scrollbar(mainframe, orient="vertical")
hsb.grid(row=27, column=2,sticky='ns')
sorted_data_text = tk.Text(mainframe,height=5,width=35, bg = "#264653",fg="white",bd=7,wrap="word",yscrollcommand=hsb.set)
sorted_data_text.insert(1.0,'Sorted Data will be Displayed Here')
sorted_data_text.grid(row=27,column=1, sticky='nsew',padx=(10,0),pady=(10,10))
hsb.config(command=sorted_data_text.yview)


#-------------------------------------MainFrame Tab => List of Algos/Complexities and Time Taken // Lot of Stuff here---------------------------------

i=4
while i<23:
    ttk.Separator(mainframe,orient='horizontal').grid(row=i,column=0,columnspan=5,sticky='we')
    i=i+2

i=3
k=1
while i<22:
    ctk.CTkLabel(mainframe,text=complexities[k]).grid(row=i,column=1)
    i=i+2
    k=k+1

tk.Label(mainframe,text="Algorithm",relief=RAISED,font=("Cambria", 15)).grid(row=2,column=0,sticky='we',pady=10)
tk.Label(mainframe,text="Theoretical Time Complexity",relief=RAISED,font=("Cambria", 15)).grid(row=2,column=1,sticky='we')
tk.Label(mainframe,text="Time taken to Sort",relief=RAISED,font=("Cambria", 15)).grid(row=2,column=2,sticky='we',columnspan=2)

ctk.CTkLabel(mainframe,text="Selection Sort").grid(row=3,column=0)
ctk.CTkLabel(mainframe,text="Bubble Sort").grid(row=5,column=0)
'''ctk.CTkLabel(mainframe,text="Insertion Sort").grid(row=5,column=1)'''
ctk.CTkLabel(mainframe,text="Merge Sort").grid(row=7,column=0)
ctk.CTkLabel(mainframe,text="Cocktail Sort").grid(row=9,column=0)
ctk.CTkLabel(mainframe,text="Heap Sort").grid(row=11,column=0)
ctk.CTkLabel(mainframe,text="PigeonHole Sort").grid(row=13,column=0)
ctk.CTkLabel(mainframe,text="Gnome Sort").grid(row=15,column=0)
ctk.CTkLabel(mainframe,text="Shell Sort").grid(row=17,column=0)
ctk.CTkLabel(mainframe,text="Odd-Even Sort").grid(row=19,column=0)
ctk.CTkLabel(mainframe,text="Cycle Sort").grid(row=21,column=0)

#-------------------------------------MainFrame Tab  => Data Row---------------------------------

about_txt = '''Program Developed By : Gurneet Singh 
Github : @Gurneet222 
A simple program made to compare some of the most common algorithms

Github Link to Program ::
_link_to_program_

To use the program, follow the following steps :: 
1. Enter the data to be sorted in the text box in MAIN MENU
2. Click on SUBMIT DATA button
3. You get the result with time taken by different algorithms

Note: Due to unforeseen reason, the program outputs the name of
wrong algorithm 1/4th of Time. Submit again when you see wrong answer.
OR, wait 3-4s before submitting again, so that python can clean
previous data.

Music Control :: 
Click on the MUTE/UNMUTE button on Top-Right Corner

Possible Future Improvements/Updates/Ideas
*More algorithms
*Option to add a user-defined algorithm from the gui
*More songs and control options
*Switch Themes Options

Got Ideas ?? Or maybe ready to contribute ??
Create a Pull Request on repo or connect me through mail'''
tk.Label(aboutframe,text=about_txt,font=("Cambria", 15),background='#292929',fg='white',justify='left').grid(row=0,column=0,sticky='ns',pady=(20,0))
vid_label = tk.Label(aboutframe)
vid_label.grid(row=0,column=1,padx=(20,50))
happy_load = tkvideo.tkvideo("media_files\qr_code_loop.mp4", vid_label, loop = 1, size = (200,200))
happy_load.play()

mainframe.grid_columnconfigure(0,weight=1)
aboutframe.grid_columnconfigure(0,weight=1)
root.mainloop()

#-------------------------------------TIME CALC SAMPLE CODE------------------------------------

'''a = dt.datetime.now()
b = dt.datetime.now()
time_diff = (b - a)
execution_time = time_diff.total_seconds() * 1000'''
