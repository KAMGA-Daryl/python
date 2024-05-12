import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

label_1 = tk.Label(root, text="Nom")
label_1.pack()

entry_1 = tk.Entry(root)
entry_1.pack()

label_2 = tk.Label(root, text="Prénom")
label_2.pack()

entry_2 = tk.Entry(root)
entry_2.pack()

label_3 = tk.Label(root, text="Adresse")
label_3.pack()

entry_3 = tk.Entry(root)
entry_3.pack()

button = tk.Button(root, text="Envoyer")
button.pack()

root.mainloop()
