
frase = input("Digite uma frase: ")
vogais = [char.lower() for char in frase if char.lower() in 'aeiou']
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']

vogais.sort()

print("Vogais:", vogais)
print("Consoantes:", consoantes)
