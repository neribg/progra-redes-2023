'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 3.2.1.11
'''
word_without_vowels = ""

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()  

word_without_vowels = ""  

for letter in user_word:
    if letter in "AEIOU": 
        continue  # Si es una vocal, salta al siguiente giro del bucle sin agregarla a word_without_vowels
    word_without_vowels += letter  

print("Palabra sin vocales:", word_without_vowels)
# Imprimir la palabra asignada a word_without_vowels.
