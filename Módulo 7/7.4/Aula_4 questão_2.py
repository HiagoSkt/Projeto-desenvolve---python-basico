import re

with open("frase.txt", "r") as arquivo:
    frase = arquivo.read()

palavras = re.findall(r"[a-zA-Z]+", frase)

with open("palavras.txt", "w") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")

with open("palavras.txt", "r") as arquivo_palavras:
    conteudo = arquivo_palavras.read()

print(conteudo)
