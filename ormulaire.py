from tkinter import *
import sqlite3

root = Tk()
root.title('Formulaire')
root.geometry('450x450')


matricule = Label(root, text="Matricule :")
prenom = Label(root, text="Prenom :")
nom = Label(root, text="Nom :")
email = Label(root, text="Email :")
tel = Label(root, text="Téléphone :")

e_matricule = Entry(root, width=35)
e_prenom = Entry(root, width=35)
e_nom = Entry(root, width=35)
e_email = Entry(root, width=35)
e_tel = Entry(root, width=35)

matricule.grid(row=0, colum=0)
e_matricule.grid(row=0, colum=1)

prenom.grid(row=1, colum=0)
e_prenom.grid(row=1, colum=1)

nom.grid(row=2, colum=0)
e_nom.grid(row=2, colum=1)

email.grid(row=3, colum=0)
e_email.grid(row=3, colum=1)

tel.grid(row=4, colum=0)
e_tel.grid(row=4, colum=1)


root.mainloop()
