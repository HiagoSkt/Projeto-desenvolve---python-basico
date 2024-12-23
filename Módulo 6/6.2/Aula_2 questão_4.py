
def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(min(len(lista1), len(lista2))):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    if len(lista1) > len(lista2):
        lista_intercalada.extend(lista1[len(lista2):])
    elif len(lista2) > len(lista1):
        lista_intercalada.extend(lista2[len(lista1):])
    
    return lista_intercalada

quantidade_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o elemento {i+1} da lista 1: ")) for i in range(quantidade_lista1)]

quantidade_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o elemento {i+1} da lista 2: ")) for i in range(quantidade_lista2)]

lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
