import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Trouver le pays du numéro
num = "+2379657257098"
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum, "fr")
print(localisation)

# trouver l'operateur mobile
operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))

# trouver la latitude et longitude
clef = "1c915cdb7b074014a583d8364d649725"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat, lng)

# creation du Map
monMap = folium.Map(location=[lat, lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save('nelson.html')