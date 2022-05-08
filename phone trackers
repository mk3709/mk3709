import phonenumbers 
from pnumber import number
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import number_type
c_number=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(c_number,'en'))

from phonenumbers import carrier
service_provider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))

from phonenumbers import timezone
time=timezone.time_zones_for_number(c_number)
print(time)
