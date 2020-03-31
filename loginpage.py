import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import os

def verif():
	ident = ID.get()
	passw = MDP.get()
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute('SELECT * FROM login')
	user_list = cursor.fetchall()
	for i in user_list:
		if ident in i:
			if passw in i:
				window.destroy()
				os.system("python Nolann.py")
		else:
			print('ERROR : Login or Password')
			print('Try Again')

window = tk.Tk()
window.title('BusinessTech')
window.geometry('1280x720')
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)

frame = Frame(window, bg='#013D6B', padx=540, pady=300)
frame2 = Frame(frame, bg='white', padx=20)


label = Label(frame2, text='CONNEXION', font=('Arial', 20), bg='white', fg='#013D6B')
label.pack()
frame2.pack()

ID = StringVar()
ID.set('Identifiant')
entry_ID = Entry(frame, textvariable=ID, width=30, bg='white')
entry_ID.pack(pady=2)

MDP = StringVar()
MDP.set('Mot de Passe')
entry_MDP = Entry(frame, textvariable=MDP, width=30)
entry_MDP.pack()

Button = Button(frame, text='LOGIN', command=verif)
Button.pack(pady=10)

frame.pack()
window.mainloop()