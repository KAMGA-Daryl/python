from tkinter import*
from PIL import Image, ImageTk

def listeInscrit(fenetre,liste):
    newFen = Toplevel(fenetre)
    newFen.geometry("350x400+350+150")
    newFenfen.title("liste des inscrits")


    listeCan = Canvas(newFen,bg="#ff7800")
    fontLabel = 'arial 13 bold'

    resultat = Label(listeCan, text=" liste des gens inscrits", font=fontLabel, fg='#ff7800', bg="white")
    prenom = Label(listeCan, text="votre prenom ",width=15, font=fontLabel, fg='white', bg="#ff7800")
    nom = Label(listeCan, text="votre nom ",width=6 ,font=fontLabel, fg='white', bg="#ff7800")
    photo = Label(listeCan, text="photo ",width=12, font=fontLabel, fg='white', bg="#ff7800")
    status = Label(listeCan, text="aucun inscrit pour le moment", font='arial 9 bold', fg='white', bg="#ff7800")

    listeCan.grid(row=0,column=0)
    resultat.grid(row=0,column=0,columnspan = 3)
    photo.grid(row=1,column=1,padx=5,pady=5)
    prenom.grid(row=1,column=2,padx=5,pady=5)
    nom.grid(row=2,column=0,columnspan= 3)
    status.grid(row=2,column=0,columnspan = 3)

    if liste:
        r=2
        for p in liste:
            photolab = Label(listeCan,height=50)
            img = Image.open(p.photo)
            img = img.resize((80,80), Image.ANTIALIAS)
            photolab.img = ImageTk.PhotoImage(img)
            photolab.configure(image=photolab.img)

            pre = Label(listeCan, text=p.prenom , font=fontLabel, fg='white', bg="#ff7800")
            no = Label(listeCan, text=p.nom, font=fontLabel, fg='white', bg="#ff7800")

            photolab.grid(row = r, column = 0,pady=2)
            pre.grid(row = r, column = 2)
            no.grid(row = r, column = 3)
            listeCan.create_line(9,55,355,55,width=1,fill='white')

            r+=1

            status.configure(text="{} inscrits pour le moment".format(len(liste)))
            status.grid(row = r, column=0,columnspan=3,pady=2)

    newFen.mainloop()








