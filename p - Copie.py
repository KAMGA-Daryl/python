import pymysql
from tkinter import *
from tkinter.messagebox import *

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="recrut"
)
def submit():
    nomp = nomp_entry.get()
    telephone = telephone_entry.get()
    adresse = adresse_entry.get()
    email = email_entry.get()
    formation = formation_entry.get()
    experience = experience_entry.get()

    mycursor = mydb.cursor()
    sql = "INSERT INTO personne (nomp,telephone,adresse,email,formation,experience) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (nomp, telephone, adresse, email, formation, experience)
    mycursor.execute(sql, val)
    mydb.commit()

# creation de fenetre
fen = Tk()
fen.title("FORMULAIRE  RECRUTEMENT")
fen.geometry("1300x1000+0+0")
fen.resizable(False, False)
fen.configure(background="lavender")

titre = Label(fen, borderwidth=3, relief=SUNKEN, text="FORMULAIRE DE PERSONNE ", font=("sans, 25"), bg="white", fg="black")
titre.place(x=400, y=0, width=600)

nomp = Label(fen, text="NOM", font=('time new rom', 10, "bold"), fg="BLACK")
nomp.place(x=0, y=200)
nomp_entry = Entry(fen, font=('time new rom', 15, "bold"), bg="white", fg="BLACK")
nomp_entry.place(x=40, y=200)

telephone = Label(fen, text="NUMERO DE TELEPHONE :", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
telephone.place(x=0, y=250)
telephone_entry = Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
telephone_entry.place(x=250, y=250)

adresse = Label(fen, text="ADRESSE :", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
adresse.place(x=0, y=300)
adresse_entry = Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
adresse_entry.place(x=100, y=300)

email = Label(fen, text="EMAIL:", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
email.place(x=0, y=350)
email_entry = Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
email_entry.place(x=80, y=350)

formation = Label(fen, text="FORMATION :", font=('time new rom', 12, "bold"), bg="blue", fg="BLACK")
formation.place(x=0, y=400)
formation_entry = Entry(fen, font=('time new rom', 12, "bold"), bg="white", fg="BLACK")
formation_entry.place(x=150, y=400)

experience = Label(fen, text="EXPERIENCE:", font=('time new rom', 15, "bold"), bg="blue", fg="BLACK")
experience.place(x=0, y=450)
experience_entry = Entry(fen, font=('time new rom', 15, "bold"), bg="white", fg="BLACK")
experience_entry.place(x=150, y=450)

#photo = PhotoImage(file="recrut.jpg")
#canvas = Canvas(fen, width=350, height=200)
#canvas.create_image(0, 0, anchor=NW, image=photo)
#canvas.pack()

def enregistrer():
    showinfo("vous avez été enregistré")
    btn = Button(fen, command=enregistrer)



#Button(text='Action', command=callback).pack()
btn = Button(fen, text="enregistrer", command=submit,  font=('time new rom', 15, "bold"), bg="purple", fg="black")
btn.place(x=200, y=500)

#btn.place(x=200, y=500)

fen.mainloop()
