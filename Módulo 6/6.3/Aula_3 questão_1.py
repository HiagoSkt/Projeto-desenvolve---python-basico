numeros = []
while len(numeros) < 4:
    numero = int(input("Digite um número inteiro (pelo menos 4 valores): "))
    numeros.append(numero)

print("Lista original:", numeros)

print("Os 3 primeiros elementos:", numeros[:3])

print("Os 2 últimos elementos:", numeros[-2:])

print("Lista invertida:", numeros[::-1])

print("Elementos de índice par:", numeros[::2])

print("Elementos de índice ímpar:", numeros[1::2])
