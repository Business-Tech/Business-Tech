import tkinter as tk
from tkinter import *
import sqlite3
import os

def delete_user():
    USER = ("'" + entry_User.get() + "'")
    horaires = sqlite3.connect('horaires.db')
    c_horaires = horaires.cursor()
    c_horaires.execute('CREATE TABLE IF NOT EXISTS t_hor (user TEXT, lundi TEXT, mardi TEXT, mercredi TEXT, jeudi TEXT, vendredi TEXT, samedi TEXT, dimanche TEXT)')
    c_horaires.execute('DELETE FROM t_hor WHERE user = ' + USER)
    horaires.commit()
    horaires.close()
    window.destroy()
    os.system('python horaires.py')

window = tk.Tk()
window.title('BusinessTech')
window.geometry('200x60')
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)

label_User = Label(window, text='ID User')
label_User.grid(column=0, row=0)
User = StringVar()
entry_User = Entry(window, textvariable=User)
entry_User.grid(column=1, row=0)
Set_User = Button(window, text='MODIFY', command=delete_user)
Set_User.grid(column=1, row=7, pady=5)

window.mainloop()