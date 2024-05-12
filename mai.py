# les bibliotheque
import pymysql
from subprocess import call
from tkinter import ttk,Tk
from tkinter import *

from tkinter import messagebox

def poste():

    fen.destroy()
    call(["python", "C:\\Users\\leandra\\PycharmProjects\\recrutement\\poste.py"])

    #call(["python", "C:\\Users\\leandra\\PycharmProjects\\recrutement\\poste.py"])

#fontion produit
def tache():

    fen.destroy()
    call(["python", "C:\\Users\\leandra\\PycharmProjects\\recrutement\\tache.py"])

#fontion fourisseur
def service():

    fen.destroy()
    call(["python", "C:\\Users\\leandra\\PycharmProjects\\recrutement\\service.py"])

#fontion commande
def departement():

    fen.destroy()
    call(["python", "C:\\Users\\leandra\\PycharmProjects\\recrutement\\departement.py"])
   # call(["python","C:\Users\leandra\PycharmProjects\recrutement\departement.py"])

#fontion facture
def p():

    fen.destroy()
    call(["python", "C:\\Users\\leandra\\PycharmProjects\\recrutement\\p.py"])
    #call(["python","C:\Users\leandra\PycharmProjects\recrutement\p.py"])




#ma fenetre

fen = Tk()
fen.title("GESTION  DE RECRUTEMENT")
fen.geometry("1300x3000")
fen.resizable(False, False)
fen.configure(background="purple")

titre = Label(fen, borderwidth=3, relief=SUNKEN, text="GESTION DE RECRUTEMENT", font=("sans, 25"), bg="black", fg="white")
titre.place(x = 400, y=0, width=600)

bouton = Button(fen, text="POSTE", bg='fuchsia',fg='black', font=('time new rom', 15, "bold"), command=poste)
bouton.place(x=0,y=100, width=200,height=150)

#bouton commande
bouton = Button(fen, text="TACHE", bg='cyan', fg='black', font=('time new rom', 15, "bold"), command=tache)
bouton.place(x=1000, y=100, width=250, height=150)

bouton = Button(fen, text="SERVICE", bg='magenta',fg='black', font=('time new rom',15 , "bold"), command=service)
bouton.place(x=0,y=300, width=250, height=100)

bouton = Button(fen, text="DEPARTEMENT", bg='teal', fg='black', font=('time new rom', 15, "bold"), command=departement)
bouton.place(x=1000, y=300, width=250, height=150)

#bouton facture
bouton = Button(fen, text="PERSONNE", bg='lavender',fg='black', font=('time new rom', 15, "bold"), command=p)
bouton.place(x=600, y=150, width=200, height=150)

fen.mainloop()




