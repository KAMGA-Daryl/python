import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Gestion des appels électroniques")

# Ajouter un champ de texte pour le nom de l'appelant
nom_label = tk.Label(fenetre, text="Nom de l'appelant : ")
nom_label.pack()
nom_entree = tk.Entry(fenetre)
nom_entree.pack()

# Ajouter un champ de texte pour le numéro de téléphone de l'appelant
numero_label = tk.Label(fenetre, text="Numéro de téléphone : ")
numero_label.pack()
numero_entree = tk.Entry(fenetre)
numero_entree.pack()

# Ajouter un bouton pour enregistrer l'appel
enregistrer_bouton = tk.Button(fenetre, text="Enregistrer l'appel")
enregistrer_bouton.pack()

fenetre.mainloop()

