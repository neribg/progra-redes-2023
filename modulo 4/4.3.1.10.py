'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 4.3.1.10
'''

def liters_100km_to_miles_gallon(liters):
    liters_per_gallon = 3.785411784
    km_per_mile = 0.621371192
    miles = 100 / (liters / liters_per_gallon)
    return miles / km_per_mile

def miles_gallon_to_liters_100km(miles):
    liters_per_gallon = 3.785411784
    km_per_mile = 0.621371192
    kilometers = miles * km_per_mile
    return liters_per_gallon / (kilometers / 100)
    
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
