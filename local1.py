import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone

gb_number = phonenumbers.parse("+237698322083"      "", "GB")
time = timezone.time_zones_for_number(gb_number)
print(time)