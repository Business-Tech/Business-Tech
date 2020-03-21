import tkinter as tk
from tkinter import*
from tkinter.ttk import*
import time
from tkinter import messagebox


window = tk.Tk()
window.title('BusinessTech')
window.geometry('1280x720')
window.resizable(width=False, height=False)
logo = PhotoImage("Image/bt.gif")

menu_sup = tk.PanedWindow(window, background='blue', height=60, width=1280, orient=HORIZONTAL)
menu_sup.pack(side=TOP,)
button_accueil = tk.Button (menu_sup, text="Accueil",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue',  width=15, justify=CENTER) 
menu_sup.add(button_accueil)
button_planning = tk.Button (menu_sup,text="Planning",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER)
menu_sup.add(button_planning)
button_com = tk.Button (menu_sup,text="Communication",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER) 
menu_sup.add(button_com)
button_salaire = tk.Button (menu_sup, text="Salaire",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER) 
menu_sup.add(button_salaire)
button_infos = tk.Menubutton (menu_sup, text="Prénom:\nNom :",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, anchor='w',)
menu_sup.add(button_infos)

logo=tk.Label(window, image=logo)
logo.pack()

# Création d'un menu défilant
deroulant_infos = Menu(button_infos, )
deroulant_infos.add_command(label="Nom",) #command = instrution#
deroulant_infos.add_command(label="Prénom", )
deroulant_infos.add_command(label="Mail", )
deroulant_infos.add_command(label="déconnexion",background='red', )

# Attribution du menu déroulant au menu Affichage
button_infos.configure(menu=deroulant_infos)

#Background
background = PhotoImage(file='Image/background.gif', master=window)
canvas = tk.Canvas(window, width=1280, height=660, background='blue',)
canvas.pack()
canvas.create_image((1280/2, 660/2), image=background)
icon = tk.PhotoImage(file='Image/background.gif')
window.iconphoto(True, icon)
window.mainloop()