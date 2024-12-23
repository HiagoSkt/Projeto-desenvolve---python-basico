import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))

print("Lista1:", lista1)
print("Lista2:", lista2)

interseccao.sort()
print("Interseccao:", interseccao)

print("Contagem:")
for num in interseccao:
    count_lista1 = lista1.count(num)
    count_lista2 = lista2.count(num)
    print(f"{num}: (lista1={count_lista1}, lista2={count_lista2})")
