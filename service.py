import pymysql
from tkinter import *

from PIL import ImageTk, Image

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="recrut"
)
def submit():
    noms = noms_entry.get()
    descriptions = descriptions_entry.get()
    duree = duree_entry.get()
    lieu = lieu_entry.get()
    disponibilite = disponibilite_entry.get()
    niveau = niveau_entry.get()
    equipement = equipement_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO service (noms,descriptions,duree,lieu,disponibilite,niveau, equipement) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (noms, descriptions, duree, lieu, disponibilite, niveau, equipement)
    mycursor.execute(sql, val)
    mydb.commit()
#def submit():
# creation de fenetre
fen = Tk()
fen.title("FORMULAIRE DE RECRUTEMENT")
fen.geometry("1300x1000+0+0")
fen.resizable(False, False)
fen.configure(background="magenta")

#ajouter le titre

titre = Label(fen, borderwidth=3, relief=SUNKEN, text="FORMULAIRE DE SERVICE", font=("sans, 25"), bg="white", fg="black")
titre.place(x=400, y=0, width=600)

noms = Label(fen, text="NOM DU SERVICE", font=('time new rom', 10, "bold"), fg="BLACK")
noms.place(x=0, y=200)
noms_entry = Entry(fen, font=('time new rom', 15, "bold"), bg="white", fg="BLACK")
noms_entry.place(x=200, y=200)

descriptions = Label(fen, text="DESCRIPTION:", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
descriptions.place(x=0, y=250)
descriptions_entry= Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
descriptions_entry.place(x=250, y=250)

duree = Label(fen, text="DUREE DE SERVICE :", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
duree.place(x=0, y=300)
duree_entry = Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
duree_entry.place(x=250, y=300)

lieu = Label(fen, text="LIEU DU SEVICE:", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
lieu.place(x=0,y=350)
lieu_entry = Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
lieu_entry.place(x=300, y=350)

disponibilite= Label(fen, text=" DISPONIBILITE:", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
disponibilite.place(x=0,y=400)
disponibilite_entry= Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
disponibilite_entry.place(x=150, y=400)

niveau= Label(fen, text="NIVEAU DE QUALITE:", font=('time new rom', 15, "bold"), bg="blue", fg="BLACK")
niveau.place(x=0,y=450)
niveau_entry= Entry(fen, font=('time new rom', 15, "bold"), bg="white", fg="BLACK")
niveau_entry.place(x=350, y=450)

equipement= Label(fen, text=" EQUIPEMENT:", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
equipement.place(x=0,y=500)
equipement_entry= Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
equipement_entry.place(x=150, y=500)

# Ajout du bouton pour valider le formulaire
btn = Button(fen, text="enregistrer", command=submit, font=('time new rom', 15, "bold"), bg="green", fg="black")
btn.place(x=200,y=600)

fen.mainloop()


