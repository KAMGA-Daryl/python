#Les Bibliotheque a importer
import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
#cd AppData\Local\Programs\Python39
#python -m pip install mysql-connector-python








#Ma fenetre
root = Tk()

root.title("FENETRE DE CONNEXION")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#091821")


#Ajouter un titre
lbltitre = Label(root, borderwidth = 3, relief = SUNKEN
                 , text = "GESTION NOTES ETUDIANTS", font = ("Sans Serif", 25),background = "#091821", fg = "#FFFAFA")
lbltitre.place(x = 0, y = 0, width = 1350, height=100)

#Detail des eleves



#Matricule
lblNumero = Label (root, text="MATRICULE", font=("Arial", 18),bg="#091821", fg="white")
lblNumero.place(x = 70, y = 200,width = 150)
txtNumero = Entry(root,bd=4, font=("Arial", 14))
txtNumero.place(x=250, y=150,width=150)

#Nom
lblNom = Label (root, text="NOM", font=("Arial", 18),bg="#091821", fg="white")
lblNom.place(x = 70, y = 150,width = 150)
txtNom = Entry(root,bd=4, font=("Arial", 14))
txtNom.place(x=250, y=150,width=300)
#Prenom
lblPrenom = Label (root, text="PRENOM", font=("Arial", 18),bg="#091821", fg="white")
lblPrenom.place(x = 70, y = 150,width = 150)
txtPrenom = Entry(root,bd=4, font=("Arial", 14))
txtPrenom.place(x=250, y=250,width=300)

#Sexe

ValeurSexe = StringVar()

lblSexeMasculin = Radiobutton(root, text="MASCULIN", value="M", variable=ValeurSexe, indicatoron=0, font=("Arial", 14),bg="#091821", fg="#696969")
lblSexeMasculin.place(x = 250, y = 350,width = 130)
txtSexeFeminin = Radiobutton(root, text="FEMININ", value="F", variable=ValeurSexe, indicatoron=0, font=("Arial", 14),bg="#091821", fg="#696969")
txtSexeFeminin.place(x=420, y=300,width=130)

#Classe
lblClasse = Label (root, text="CLASSE", font=("Arial", 18),bg="#091821", fg="white")
lblClasse.place(x = 70, y = 350,width = 150)

comboClasse = ttk.Combobox(root, font=("Arial", 14))
comboClasse['values'] = ['CP','CE1','CE2','CM1','CM2','6e','5e','4e','3e']
comboClasse.place(x=250, y=350,width=130)
#Matiere
lblMatiere = Label (root, text="MATIERE", font=("Arial", 18),bg="#091821", fg="white")
lblMatiere.place(x = 70, y = 400,width = 150)
txtMatiere = Entry(root,bd=4, font=("Arial", 14))
txtMatiere.place(x=250, y=400,width=300)

#note
lblnote = Label (root, text="NOTE", font=("Arial", 18),bg="#091821", fg="white")
lblnote.place(x = 70, y = 450,width = 150)
txtnote = Entry(root,bd=4, font=("Arial", 14))
txtnote.place(x=250, y=450,width=200)


#Enregistrer
btnenregistrer = Button(root, text="Enregistrer", font=("Arial", 16),bg="#091821", fg="white" )
btnenregistrer.place(x=250, y=500,width=200)

#modifier
btnmodifier = Button(root, text="modifier", font=("Arial", 16),bg="#091821", fg="white",)
btnmodifier.place(x=250, y=550,width=200)

#Supprimer
btnSupprimer = Button(root, text="Supprimer", font=("Arial", 16),bg="#091821", fg="white")
btnSupprimer.place(x=250, y=600,width=200)

#Table
table = ttk.Treeview(root, columns= (1, 2, 3, 4, 5, 6, 7), height = 5, show = "headings")



#Entete
table.heading(1 , text = "MAT")
table.heading(2 , text = "NOM")
table.heading(3 , text = "PRENOM")
table.heading(4 , text = "SEXE")
table.heading(5 , text = "CLASSE")
table.heading(6 , text = "MATIERE")
table.heading(7 , text = "NOTE")

#definir les dimensions des colonnes
table.column(1, width = 50)
table.column(2, width = 150)
table.column(3, width = 150)
table.column(4, width = 100)
table.column(5, width = 50)
table.column(6, width = 100)
table.column(7, width = 50)

#afficher les informations de la table
maBase = mysql.connnector.connect(host="localhost", user="root",password="", database="note_eleve")
meConnect = maBase.curser()
meConnect.execute("select * from note")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()    













#Execution
root.mainloop()