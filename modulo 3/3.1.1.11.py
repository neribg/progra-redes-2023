﻿'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 2.2.1.11
'''

ingreso= float(input("Introduce el ingreso anual:"))

if ingreso <= 85528:
    tax = (0.18 * ingreso - 556.02)
else:
    tax =(14839.02 + 0.32*(ingreso - 85528))
if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")