'''
 Alumno: Felipe Neri Francisco Bueno gonzález
 Fecha: 2 de octubre de 2023
 Descripcion: No de lista impar El tremendo SAT
'''
cantidad = int(input("ingresa la cantidad: "))
def calcular_impuesto(cantidad):
    if cantidad <= 0:
        return "La cantidad debe ser mayor a cero"
    
    if cantidad < 10000:
        impuesto = cantidad * 0.05
    elif cantidad >= 10000 and cantidad < 20000:
        impuesto = cantidad * 0.15
    elif cantidad >= 20000 and cantidad < 35000:
        impuesto = cantidad * 0.20
    elif cantidad >= 35000 and cantidad < 60000:
        impuesto = cantidad * 0.30
    else:
        impuesto = cantidad * 0.45
    
    return impuesto

print("Impuesto para $", cantidad, "es:", calcular_impuesto(cantidad))
