import tkinter as tk
from tkinter import *
import sqlite3

def update():
    horaires = sqlite3.connect('Database/horaires.db')
    c_horaires = horaires.cursor()
    c_horaires.execute('CREATE TABLE IF NOT EXISTS t_hor (user TEXT, lundi TEXT, mardi TEXT, mercredi TEXT, jeudi TEXT, vendredi TEXT, samedi TEXT, dimanche TEXT, lundi0 TEXT, mardi0 TEXT, mercredi0 TEXT, jeudi0 TEXT, vendredi0 TEXT, samedi0 TEXT, dimanche0 TEXT)')
    c_horaires.execute('INSERT INTO t_hor VALUES (:user, :lundi, :mardi, :mercredi, :jeudi, :vendredi, :samedi, :dimanche, :lundi0, :mardi0, :mercredi0, :jeudi0, :vendredi0, :samedi0, :dimanche0)',
    {
        'user':entry_User.get(),
        'lundi':entry_Lundi.get(),
        'mardi':entry_Mardi.get(),
        'mercredi':entry_Mercredi.get(),
        'jeudi':entry_Jeudi.get(),
        'vendredi':entry_Vendredi.get(),
        'samedi':entry_Samedi.get(),
        'dimanche':entry_Dimanche.get(),
        'lundi0':entry_Lundi0.get(),
        'mardi0':entry_Mardi0.get(),
        'mercredi0':entry_Mercredi0.get(),
        'jeudi0':entry_Jeudi0.get(),
        'vendredi0':entry_Vendredi0.get(),
        'samedi0':entry_Samedi0.get(),
        'dimanche0':entry_Dimanche0.get()
    })
    horaires.commit()
    horaires.close()
    window.destroy()

window = tk.Tk()
window.title('BusinessTech')
window.geometry('390x190')
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)

frame_ID = Frame(window)
frame_days = Frame(window)
frame_update = Frame(window)
frame_ID.grid(column=0, row=0)
frame_days.grid(column=0, row=1)
frame_update.grid(column=0, row=2)

label_User = Label(frame_ID, text='ID User')
label_User.grid(column=0, row=0)
label_Lundi = Label(frame_days, text='Lundi        -->')
label_Lundi.grid(column=0, row=0)
label_Mardi = Label(frame_days, text='Mardi        -->')
label_Mardi.grid(column=0, row=1)
label_Mercredi = Label(frame_days, text='Mercredi  -->')
label_Mercredi.grid(column=0, row=2)
label_Jeudi = Label(frame_days, text='Jeudi        -->')
label_Jeudi.grid(column=0, row=3)
label_Vendredi = Label(frame_days, text='Vendredi  -->')
label_Vendredi.grid(column=0, row=4)
label_Samedi = Label(frame_days, text='Samedi     -->')
label_Samedi.grid(column=0, row=5)
label_Dimanche = Label(frame_days, text='Dimanche -->')
label_Dimanche.grid(column=0, row=6)

ll = Label(frame_days, text='/')
ll.grid(column=2, row=0)
lma = Label(frame_days, text='/')
lma.grid(column=2, row=1)
lme = Label(frame_days, text='/')
lme.grid(column=2, row=2)
lj = Label(frame_days, text='/')
lj.grid(column=2, row=3)
lv = Label(frame_days, text='/')
lv.grid(column=2, row=4)
ls = Label(frame_days, text='/')
ls.grid(column=2, row=5)
ld = Label(frame_days, text='/')
ld.grid(column=2, row=6)

User = StringVar()
entry_User = Entry(frame_ID, textvariable=User)
entry_User.grid(column=1, row=0)
Lundi = StringVar()
Lundi.set('.................')
entry_Lundi = Entry(frame_days, textvariable=Lundi)
entry_Lundi.grid(column=1, row=0)
Mardi = StringVar()
Mardi.set('................')
entry_Mardi = Entry(frame_days, textvariable=Mardi)
entry_Mardi.grid(column=1, row=1)
Mercredi = StringVar()
Mercredi.set('................')
entry_Mercredi = Entry(frame_days, textvariable=Mercredi)
entry_Mercredi.grid(column=1, row=2)
Jeudi = StringVar()
Jeudi.set('................')
entry_Jeudi = Entry(frame_days, textvariable=Jeudi)
entry_Jeudi.grid(column=1, row=3)
Vendredi = StringVar()
Vendredi.set('................')
entry_Vendredi = Entry(frame_days, textvariable=Vendredi)
entry_Vendredi.grid(column=1, row=4)
Samedi = StringVar()
Samedi.set('................')
entry_Samedi = Entry(frame_days, textvariable=Samedi)
entry_Samedi.grid(column=1, row=5)
Dimanche = StringVar()
Dimanche.set('................')
entry_Dimanche = Entry(frame_days, textvariable=Dimanche)
entry_Dimanche.grid(column=1, row=6)
Lundi0 = StringVar()
Lundi0.set('................')
entry_Lundi0 = Entry(frame_days, textvariable=Lundi0)
entry_Lundi0.grid(column=3, row=0)
Mardi0 = StringVar()
Mardi0.set('................')
entry_Mardi0 = Entry(frame_days, textvariable=Mardi0)
entry_Mardi0.grid(column=3, row=1)
Mercredi0 = StringVar()
Mercredi0.set('................')
entry_Mercredi0 = Entry(frame_days, textvariable=Mercredi0)
entry_Mercredi0.grid(column=3, row=2)
Jeudi0 = StringVar()
Jeudi0.set('................')
entry_Jeudi0 = Entry(frame_days, textvariable=Jeudi0)
entry_Jeudi0.grid(column=3, row=3)
Vendredi0 = StringVar()
Vendredi0.set('................')
entry_Vendredi0 = Entry(frame_days, textvariable=Vendredi0)
entry_Vendredi0.grid(column=3, row=4)
Samedi0 = StringVar()
Samedi0.set('................')
entry_Samedi0 = Entry(frame_days, textvariable=Samedi0)
entry_Samedi0.grid(column=3, row=5)
Dimanche0 = StringVar()
Dimanche0.set('................')
entry_Dimanche0 = Entry(frame_days, textvariable=Dimanche0)
entry_Dimanche0.grid(column=3, row=6)

update = Button(frame_update, text='UPDATE', command=update)
update.grid(column=1, row=8, ipadx=40, pady=5)

window.mainloop()