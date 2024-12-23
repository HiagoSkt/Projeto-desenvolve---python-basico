
def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()

anagramas = [palavra for palavra in palavras if sao_anagramas(palavra, palavra_objetivo)]

print(f"Anagramas: {anagramas}")
