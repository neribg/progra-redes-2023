''''
  Nombre: Felipe Neri Francisco Bueno González
  Fecha: 9 de octubre de 2023
  Descripción: ejercicio de practica 3 
'''

datos = []

for i in range(5):
    num = int(input(f"Ingrese el dato {i+1}: "))
    datos.append(num)

tuplaDatos = tuple(datos)

def despliega_tupla(tupla):
    print("El contenido de la tupla:")
    for i in tupla:
        print(i)

despliega_tupla(tuplaDatos)

def suma_datos(tupla):
    suma = sum(tupla)
    print(f"La suma de los datos es: {suma}")
    return suma

suma_datos(tuplaDatos)

def multiplica_datos(tupla):
    producto = 1
    for i in tupla:
        producto *= i
    print(f"El producto de los datos es: {producto}")
    return producto

multiplica_datos(tuplaDatos)
