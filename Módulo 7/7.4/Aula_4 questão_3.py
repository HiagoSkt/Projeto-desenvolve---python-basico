import re

def contar_personagens(texto):
    nonato_count = len(re.findall(r'\bNonato\b', texto, re.IGNORECASE))
    iria_count = len(re.findall(r'\bÍria\b', texto, re.IGNORECASE))
    return nonato_count, iria_count

with open('estomago.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    
    print("Primeiras 25 linhas do arquivo:")
    for i in range(min(25, len(linhas))):
        print(linhas[i], end='')

    num_linhas = len(linhas)
    print(f"\nNúmero total de linhas: {num_linhas}")
    
    linha_com_mais_caracteres = max(linhas, key=len)
    print(f"\nLinha com maior número de caracteres:\n{linha_com_mais_caracteres.strip()}")
    
    texto_completo = ''.join(linhas)
    nonato, iria = contar_personagens(texto_completo)
    print(f"\nNúmero de menções a 'Nonato': {nonato}")
    print(f"Número de menções a 'Íria': {iria}")
