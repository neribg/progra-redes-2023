'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 3.1.1.12
'''

year = int(input("Introduce un año:"))

if year < 1582:
    print(" No esta dentro del período del calendario Gregoriano")
else:
  if year%4 !=0:
     print("Año común")
  elif year%100 !=0:
         print("año bisiesto")
  elif year%400 !=0:
         print("año común")
  else:
        print("año bisiesto")
#
# Escribe tu código aquí.
#	
