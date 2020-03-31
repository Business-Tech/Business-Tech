import tkinter as tk
from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
import sqlite3
import time
import os

def logout():
	user = sqlite3.connect('user_database.db')
	cur = user.cursor()
	cur.execute('DELETE FROM us_er')
	user.commit()
	user.close()
	window.destroy()
	os.system('python loginpage.py')

user = sqlite3.connect('user_database.db')
cur = user.cursor()
cur.execute('SELECT * FROM us_er')
first_username = cur.fetchone()[0]
cur.execute('SELECT * FROM us_er')
last_username = cur.fetchone()[1]
user.commit()
user.close()

window = tk.Tk()
window.title('BusinessTech')
window.geometry('1280x720')
window.resizable(width=False, height=False)
logo = PhotoImage("Image/bt.gif")

identity = ("Nom : " +last_username + "\n Prénom : " + first_username)

menu_sup = tk.PanedWindow(window, background='blue', height=60, width=1280, orient=HORIZONTAL, bd=0)
menu_sup.pack(side=TOP)
button_accueil = tk.Button (menu_sup, text="Accueil",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue',  width=15, justify=CENTER) 
menu_sup.add(button_accueil)
button_planning = tk.Button (menu_sup,text="Planning",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER)
menu_sup.add(button_planning)
button_com = tk.Button (menu_sup,text="Communication",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER) 
menu_sup.add(button_com)
button_salaire = tk.Button (menu_sup, text="Salaire",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER) 
menu_sup.add(button_salaire)
button_infos = tk.Menubutton (menu_sup, text=identity,foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, anchor='w',)
menu_sup.add(button_infos)

logo=tk.Label(window, image=logo)
logo.pack()

# Création d'un menu défilant
deroulant_infos = Menu(button_infos, )
deroulant_infos.add_command(label="Nom",) #command = instrution#
deroulant_infos.add_command(label="Prénom", )
deroulant_infos.add_command(label="Mail", )
deroulant_infos.add_command(label="déconnexion",background='red', command=logout)

# Attribution du menu déroulant au menu Affichage
button_infos.configure(menu=deroulant_infos)

#Background
background = PhotoImage(file='Image/background.gif', master=window)
canvas = tk.Canvas(window, width=1280, height=660, background='blue', bd=0, highlightthickness=0)
canvas.pack()
canvas.create_image((1280/2, 660/2), image=background)
icon = tk.PhotoImage(file='Image/background.gif')
window.iconphoto(True, icon)
window.mainloop()