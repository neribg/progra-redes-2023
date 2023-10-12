﻿'''
 Alumno: Felipe Neri Francisco Bueno gonzález
 Fecha: 2 de octubre de 2023
 Descripcion: No de lista impar Jugando con listas
'''

subjects = ["Probabilidad y Estadística", 
"Electrónica para IDC Física", 
"Conexión de redes WAN",
"Administración de servidores I", 
"Programación de Redes",
"Inglés IV"]
grades = []

for subject in subjects:
    grade = input("¿Cuál fue tu nota en la unidad I de " + subject + "? ")
    grades.append(grade)

for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + grades[i])