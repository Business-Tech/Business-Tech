from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
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

	def message():
		user = sqlite3.connect('user_database.db')
		cur = user.cursor()
		cur.execute('SELECT * FROM us_er')
		current_user = cur.fetchone()[0]

		ID_Dest = entry_Dest.get()
		IDest = str(ID_Dest)

		db_message = sqlite3.connect('message.db')
		cursor_message = db_message.cursor()
		cursor_message.execute('CREATE TABLE IF NOT EXISTS notes (message TEXT, byy TEXT, too TEXT)')
		cursor_message.execute('INSERT INTO notes VALUES (:message, :byy, :too)',
			{
				'message':entry.get(),
				'byy':current_user,
				'too':IDest
			})
		db_message.commit()
		db_message.close()
		communication()
	
	def remove():
		db_message = sqlite3.connect('message.db')
		cursor_message = db_message.cursor()
		cursor_message.execute('DELETE FROM notes')
		db_message.commit()
		db_message.close()
		communication()

	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute('SELECT id, last_name, first_name FROM login')
	id_verif = cursor.fetchone()[0]
	names = cursor.fetchall()

	user = sqlite3.connect('user_database.db')
	cur = user.cursor()
	cur.execute('SELECT * FROM us_er')
	current_user = cur.fetchone()[0]

	db_message = sqlite3.connect('message.db')
	cursor_message = db_message.cursor()
	cursor_message.execute('CREATE TABLE IF NOT EXISTS notes (message TEXT, byy TEXT, too TEXT)')
	cursor_message.execute('SELECT byy FROM notes')
	byy_verif = cursor_message.fetchall()
	cursor_message.execute('SELECT too FROM notes')
	too_verif = cursor_message.fetchall()

	lock_byy=''
	for b in byy_verif:
		if current_user in b:
			db_message = sqlite3.connect('message.db')
			cursor_message = db_message.cursor()
			VERIF = ("'" + current_user + "'")
			cursor_message.execute("SELECT * FROM notes WHERE byy = " + VERIF)
			lock_byy = cursor_message.fetchall()

	lock_too=''
	for t in too_verif:
		if current_user in t:
			db_message = sqlite3.connect('message.db')
			cursor_message = db_message.cursor()
			VERIF = ("'" + current_user + "'")
			cursor_message.execute("SELECT * FROM notes WHERE too = " + VERIF)
			lock_too = cursor_message.fetchall()

	full_mess_by=''
	for fb in lock_byy:
		full_mess_by += str(fb) + '\n'

	full_mess_to=''
	for ft in lock_too:
		full_mess_to += str(ft) + '\n'

	l1 = Label(frame_communication, bg='#013D6B')
	l1.grid(column=0, row=1)
	load = Image.open("Image/message_box.png")
	render = ImageTk.PhotoImage(load)
	img = Label(frame_communication, image=render)
	img.image = render
	img.grid(column=0, row=2)

	Destinataire = StringVar()
	entry_Dest = Entry(frame_communication, textvariable=Destinataire, width=10, bg='white')
	entry_Dest.grid(column=1, row=2, sticky=W, ipadx=4, padx=312)
	print_Dest = Label(frame_communication, text='ID Destinataire :')
	print_Dest.grid(column=1, row=2, sticky=W, padx=220)

	frame_users = Frame(frame_communication)
	frame_users.grid(column=0, row=3, sticky=W, ipadx=304, ipady=260, padx=18, pady=15)
	frame_users.grid_propagate(0)
	frame_text = Frame(frame_communication)
	frame_text.grid(column=1, row=3, sticky=W, ipadx=298, ipady=260, padx=15)
	frame_text.grid_propagate(0)

	table = ttk.Treeview(frame_users, columns=(1,2,3), show='headings', height=26)
	table.grid()
	table.heading(1, text='ID')
	table.heading(2, text='Nom')
	table.heading(3, text='Prénom')
	for n in names:
		table.insert('', 'end', values=n)

	Text = StringVar()
	Text.set('Say Something')
	entry = Entry(frame_communication, textvariable=Text, width=30, bg='white')
	entry.grid(column=1, row=4, sticky=W, ipadx=172, ipady=4, padx=10)
	Buttonn = Button(frame_communication, text='-->', command=message)
	Buttonn.grid(column=1, row=4, sticky=W, padx=575)
	Text_Remove = Label(frame_communication, text='Cliquer sur ce bouton                 pour supprimer la conversation')
	Text_Remove.grid(column=0, row=4, sticky=W, ipadx=136, ipady=5, padx=18)
	Buttonn_remove = Button(frame_communication, text='O', command=remove)
	Buttonn_remove.grid(column=0, row=4, sticky=W, padx=280)
	full_mess = full_mess_by + full_mess_to
	query_text = Label(frame_text, text=full_mess)
	query_text.grid()

	msg_frame = Frame(frame_text)
	msg_frame.grid(column=1, row=3)
	

def salaire():
	destroy_window()
	frame_salaire.grid()
	#code here :

user = sqlite3.connect('user_database.db')
cur = user.cursor()
cur.execute('SELECT * FROM us_er')
first_username = cur.fetchone()[1]
cur.execute('SELECT * FROM us_er')
last_username = cur.fetchone()[2]
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