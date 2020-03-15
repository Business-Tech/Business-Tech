import tkinter as tk
from tkinter import*
from tkinter.ttk import*
import time

def progress():  
    x = 0
    for i in range(0,100):
    	x+=1
    	PgBar['value'] = x 
    	window.update_idletasks() 
    	time.sleep(0.05)

window = tk.Tk()
window.title('BusinessTech')
window.geometry('1280x720')
window.resizable(width=False, height=False)

image = PhotoImage(file='/home/lucien/Documents/Python/BusinessTech/bt.png', master=window)
canvas = Canvas(window, width=1280, height=650)
canvas.pack()
canvas.create_image((1280//2, 720//2), image=image)
icon = tk.PhotoImage(file='/home/lucien/Documents/Python/BusinessTech/bt.png')
window.iconphoto(True, icon)

PgBar = Progressbar(window, orient='horizontal', length=500, maximum=100)  
PgBar.pack()
progress()

window.mainloop()
