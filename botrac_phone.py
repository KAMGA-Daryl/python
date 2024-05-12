import tkinter
import tkintermapview
import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox

root = tkinter.TK()
root.geometry("500x500")

label1 = Label1(text="Phone Number Tracker")
label1.pack()

number = text (height=1)
number.pack()

button = Button(text="search")
button.pack(pady = 10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()