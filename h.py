from tkinter import *
from import pyodbc 

root = Tk()
root.title("Formulaire d'enregistrement")

# Établir une connexion avec la base de données Access
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\LIONEL PC\Documents\Database3.accdb;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


# Création des champs de saisie
id_page_label = Label(root, text="ID Page")
id_page_entry = Entry(root)
nom_page_label = Label(root, text="Nom Page")
nom_page_entry = Entry(root)
type_page_label = Label(root, text="Type Page")
type_page_entry = Entry(root)
nb_followers_label = Label(root, text="Nombre de Followers")
nb_followers_entry = Entry(root)
id_publication_label = Label(root, text="ID Publication")
id_publication_entry = Entry(root)
type_publication_label = Label(root, text="Type Publication")
type_publication_entry = Entry(root)
date_publication_label = Label(root, text="Date Publication")
date_publication_entry = Entry(root)
date_decompte_label = Label(root, text="Date Décompte")
date_decompte_entry = Entry(root)
commentaire_label = Label(root, text="Commentaire")
commentaire_entry = Entry(root)
likes_label = Label(root, text="Likes")
likes_entry = Entry(root)
partage_label = Label(root, text="Partage")
partage_entry = Entry(root)
vues_label = Label(root, text="Vues")
vues_entry = Entry(root)

# Placement des champs de saisie
id_page_label.grid(row=0, column=0)
id_page_entry.grid(row=0, column=1)
nom_page_label.grid(row=1, column=0)
nom_page_entry.grid(row=1, column=1)
type_page_label.grid(row=2, column=0)
type_page_entry.grid(row=2, column=1)
nb_followers_label.grid(row=3, column=0)
nb_followers_entry.grid(row=3, column=1)
id_publication_label.grid(row=4, column=0)
id_publication_entry.grid(row=4, column=1)
type_publication_label.grid(row=5, column=0)
type_publication_entry.grid(row=5, column=1)
date_publication_label.grid(row=6, column=0)
date_publication_entry.grid(row=6, column=1)
date_decompte_label.grid(row=7, column=0)
date_decompte_entry.grid(row=7,column=1)
commentaire_label.grid(row=8,column=0)
commentaire_entry.grid(row=8,column=1)
likes_label.grid(row=9,column=0)
likes_entry.grid(row=9,column=1)
partage_label.grid(row=10,column=0)
partage_entry.grid(row=10,column=1)
vues_label.grid(row=11,column=0)
vues_entry.grid(row=11,column=1)

# Fonction appelée lorsque le bouton "Soumettre" est cliqué
def submit():
    # Récupérer les valeurs saisies dans l'interface
    id_page = id_page_entry.get()
    nom_page = nom_page_entry.get()
    type_page = type_page_entry.get()
    nombre_followers = nb_followers_entry.get()
    id_publication = id_publication_entry.get()
    type_publication = type_publication_entry.get()
    date_publication = date_publication_entry.get()
    date_decompte = date_decompte_entry.get()
    commentaires = commentaire_entry.get()
    likes = likes_entry.get()
    partages = partage_entry.get()
    vues = vues_entry.get()

    # Insérer les données dans la base de données
    cursor.execute("INSERT INTO ma_table (id_page, type_page, nom_page, nombre_followers, id_publication, type_publication, date_publication, date_decompte, likes, commentaires, vues, partages) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id_page, type_page, nom_page, nombre_followers, id_publication, type_publication, date_publication, date_decompte, likes, commentaires, vues, partages))
    conn.commit()

# Création du bouton de soumission
submit_button = Button(root, text="Soumettre", bg="green", command=submit)
submit_button.grid(row=12, column=0, columnspan=2)

# Fonction appelée lorsque le bouton "Annuler" est cliqué
def cancel():
    # Ajoutez ici le code pour annuler l'opération en cours
    print("Opération annulée")


# Création du bouton "Annuler"
cancel_button = Button(root, text="Annuler", bg="red", command=cancel)
cancel_button.grid(row=12, column=1)

root.mainloop()

# Fermer la connexion à la base de données lorsque l'application se termine
conn.close()