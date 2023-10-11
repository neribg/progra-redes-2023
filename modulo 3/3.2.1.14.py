'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 3.2.1.14
'''
blocks = int(input("Ingresa el número de bloques: "))

height = 0
total_blocks = 0

while total_blocks < blocks:
    height += 1
    total_blocks += height

if total_blocks > blocks:
    height -= 1

print("La altura de la pirámide:", height)
