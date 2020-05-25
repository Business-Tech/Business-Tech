import tkinter as tk
from tkinter import *
import sqlite3

def update():
    horaires = sqlite3.connect('horaires.db')
    c_horaires = horaires.cursor()
    c_horaires.execute('CREATE TABLE IF NOT EXISTS t_hor (lundi TEXT, mardi TEXT, mercredi TEXT, jeudi TEXT, vendredi TEXT, samedi TEXT, dimanche TEXT)')
    c_horaires.execute('INSERT INTO t_hor VALUES (:lundi, :mardi, :mercredi, :jeudi, :vendredi, :samedi, :dimanche)',
    {
        'lundi':entry_Lundi.get(),
        'mardi':entry_Mardi.get(),
        'mercredi':entry_Mercredi.get(),
        'jeudi':entry_Jeudi.get(),
        'vendredi':entry_Vendredi.get(),
        'samedi':entry_Samedi.get(),
        'dimanche':entry_Dimanche.get()
    })
    horaires.commit()
    horaires.close()

window = tk.Tk()
window.title('BusinessTech')
window.geometry('230x170')
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)

label_Lundi = Label(window, text='Lundi        -->')
label_Lundi.grid(column=0, row=0)
label_Mardi = Label(window, text='Mardi        -->')
label_Mardi.grid(column=0, row=1)
label_Mercredi = Label(window, text='Mercredi  -->')
label_Mercredi.grid(column=0, row=2)
label_Jeudi = Label(window, text='Jeudi        -->')
label_Jeudi.grid(column=0, row=3)
label_Vendredi = Label(window, text='Vendredi  -->')
label_Vendredi.grid(column=0, row=4)
label_Samedi = Label(window, text='Samedi     -->')
label_Samedi.grid(column=0, row=5)
label_Dimanche = Label(window, text='Dimanche -->')
label_Dimanche.grid(column=0, row=6)

Lundi = StringVar()
entry_Lundi = Entry(window, textvariable=Lundi)
entry_Lundi.grid(column=1, row=0)
Mardi = StringVar()
entry_Mardi = Entry(window, textvariable=Mardi)
entry_Mardi.grid(column=1, row=1)
Mercredi = StringVar()
entry_Mercredi = Entry(window, textvariable=Mercredi)
entry_Mercredi.grid(column=1, row=2)
Jeudi = StringVar()
entry_Jeudi = Entry(window, textvariable=Jeudi)
entry_Jeudi.grid(column=1, row=3)
Vendredi = StringVar()
entry_Vendredi = Entry(window, textvariable=Vendredi)
entry_Vendredi.grid(column=1, row=4)
Samedi = StringVar()
entry_Samedi = Entry(window, textvariable=Samedi)
entry_Samedi.grid(column=1, row=5)
Dimanche = StringVar()
entry_Dimanche = Entry(window, textvariable=Dimanche)
entry_Dimanche.grid(column=1, row=6)

update = Button(window, text='UPDATE', command=update)
update.grid(column=1, row=7, pady=5)

window.mainloop()