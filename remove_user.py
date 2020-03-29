import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
import sqlite3

def remove_user():
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	PASS = ("'" + ID.get() + "'")
	cursor.execute("DELETE FROM login WHERE id = " + PASS)
	db.commit()
	db.close()

window = tk.Tk()
window.title('BusinessTech')
window.geometry('230x70')
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file='bt.gif')
window.iconphoto(True, icon)

ID = StringVar()
ID.set('IDENTIFIANT')
entry_ID = Entry(window, textvariable=ID, width=30, bg='white')
entry_ID.pack(pady=2)

Button = Button(window, text='REMOVE USER', command=remove_user)
Button.pack(pady=10)

window.mainloop()