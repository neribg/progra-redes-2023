'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 3.2.1.15
'''

c0 = int(input("Ingresa un número natural: "))
steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

print("Número de pasos:", steps)
