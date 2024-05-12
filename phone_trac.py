import phonenumbers
from geopy.geocoders import Nominatim

phone_number = "+33612345678"
parsed_number = phonenumbers.parse(phone_number)
geolocator = Nominatim(user_agent="geoapiExercises")

location = geolocator.geocode(parsed_number)
print(location.address)
