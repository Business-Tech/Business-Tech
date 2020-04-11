from tkinter import*
import tkinter as tk
import tkinter.messagebox as tm
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

def destroy_window():
	for w in frame_accueil.winfo_children():
		w.destroy()
		frame_accueil.grid_forget()
	for x in frame_planning.winfo_children():
		x.destroy()
		frame_planning.grid_forget()
	for y in frame_communication.winfo_children():
		y.destroy()
		frame_communication.grid_forget()
	for z in frame_salaire.winfo_children():
		z.destroy()
		frame_salaire.grid_forget()

def accueil():
	destroy_window()
	frame_accueil.grid()
	#code here :

def planning():
	destroy_window()
	frame_planning.grid()
	#code here :

def communication():
	destroy_window()
	frame_communication.grid()
	#code here :

	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute('SELECT first_name, last_name FROM login')
	names = cursor.fetchall()

	full_names=''
	for n in names:
		full_names += str(n) + '\n'w

	Destinataire = StringVar()
	Destinataire.set('Destinataire')
	entry_Dest = Entry(frame_communication, textvariable=Destinataire, width=30, bg='white')
	entry_Dest.grid(column=1, row=1, sticky=W, ipadx=195, padx=10)
	Objet = StringVar()
	Objet.set('Objet')
	entry_Obj = Entry(frame_communication, textvariable=Objet, width=30, bg='white')
	entry_Obj.grid(column=1, row=2, sticky=W, ipadx=195, padx=10)
	query_users = Label(frame_communication, text=full_names)
	query_users.grid(column=0, row=3, sticky=W, ipadx=250, ipady=285, padx=10)
	query_text = Label(frame_communication)
	query_text.grid(column=1, row=3, sticky=W, ipadx=300, ipady=310, padx=10)

def salaire():
	destroy_window()
	frame_salaire.grid()
	#code here :

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
window.config(background='#013D6B')
window.resizable(width=False, height=False)

identity = ("Nom : " +last_username + "\n Prénom : " + first_username)

frame_accueil = Frame(window, bg='#013D6B')
frame_accueil.grid()
frame_planning = Frame(window, bg='#013D6B')
frame_planning.grid()
frame_communication = Frame(window, bg='#013D6B')
frame_communication.grid()
frame_salaire = Frame(window, bg='#013D6B')
frame_salaire.grid()


menu_sup = tk.PanedWindow(window, background='blue', height=60, width=1280, orient=HORIZONTAL, bd=0)
menu_sup.grid(column=0,row=0, sticky=W)
button_accueil = tk.Button (menu_sup, text="Accueil",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue',  width=15, justify=CENTER, command=accueil) 
menu_sup.add(button_accueil)
button_planning = tk.Button (menu_sup,text="Planning",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER, command=planning)
menu_sup.add(button_planning)
button_com = tk.Button (menu_sup,text="Communication",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER, command=communication) 
menu_sup.add(button_com)
button_salaire = tk.Button (menu_sup, text="Salaire",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER, command=salaire) 
menu_sup.add(button_salaire)
button_infos = tk.Menubutton (menu_sup, text=identity,foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, anchor='w',)
menu_sup.add(button_infos)

# Création d'un menu défilant
deroulant_infos = Menu(button_infos, )
deroulant_infos.add_command(label="Nom",) #command = instrution#
deroulant_infos.add_command(label="Prénom", )
deroulant_infos.add_command(label="Mail", )
deroulant_infos.add_command(label="déconnexion",background='red', command=logout)

# Attribution du menu déroulant au menu Affichage
button_infos.configure(menu=deroulant_infos)

#Background
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)
window.mainloop()