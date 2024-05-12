import phonenumbers
from phonenumbers import carrier, geocoder, timezone

phone_num = input("EntreZ le numéro du téléphone à traquer: ")

phone_num = phonenumbers.parse(phone_num)

print("Zone géographique : ", timezone.time_zones_for_number(phone_num))

print("Opérateur", carrier.name_for_number(phone_num, "fr"))

print("Région géographique ", geocoder.description_for_number(phone_num, "fr"))

print("Ce numéro est valide : ",phonenumbers.is_valid_number(phone_num))

print("Possibilité de ce numero : ", phonenumbers.is_possible_number(phone_num))

