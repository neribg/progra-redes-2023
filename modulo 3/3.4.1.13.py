'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 3.4.1.13
'''

# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3
for _ in range(2):  # Se repite dos veces para agregar a Stu Sutcliffe y Pete Best.
    member = input("Agrega un miembro de la banda: ")
    beatles.append(member)
print("Paso 3:", Beatles)

# paso 4
del beatles[3]
del beatles[3]
print("Paso 4:", Beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Beatles:", beatles)
print("Número de miembros en la banda:", len(beatles))
print("Los Fav", len(Beatles))
