import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

max_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

for i in range(len(lista) - 2):
    negativos = sum(1 for x in lista[i:i+3] if x < 0)
    
    if negativos > max_negativos:
        max_negativos = negativos
        inicio_intervalo = i
        fim_intervalo = i + 3

del lista[inicio_intervalo:fim_intervalo]

print("Editada:", lista)
