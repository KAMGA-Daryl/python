import tkinter
import tkintermapview
import phonenumbers
from phonenumbers import geocoder

# Créer la fenêtre tkinter
root_tk = tkinter.Tk()
root_tk.geometry("800x600")
root_tk.title("Géolocalisation des numéros de téléphone")

# Créer le widget de la carte
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Créer le champ d'entrée du numéro de téléphone
phone_entry = tkinter.Entry(root_tk)
phone_entry.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# Créer le bouton pour géolocaliser le numéro
def geolocate():
    # Récupérer le numéro saisi
    phone_number = phone_entry.get()
    # Valider le numéro et obtenir son pays
    phone = phonenumbers.parse(phone_number)
    country = geocoder.country_name_for_number(phone, "fr")
    # Afficher le pays dans la console
    print(f"Le numéro {phone_number} appartient au pays {country}")
    # Obtenir la latitude et la longitude du pays
    lat, lon = geocoder.country_lat_long_for_number(phone)
    # Afficher la position sur la carte avec un marqueur
    map_widget.set_position(lat, lon, 5)
    map_widget.create_marker(lat, lon)

geolocate_button = tkinter.Button(root_tk, text="Géolocaliser", command=geolocate)
geolocate_button.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

# Lancer la boucle principale
root_tk.mainloop()