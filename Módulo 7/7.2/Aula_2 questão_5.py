import random

def embaralhar_palavras(frase):
    palavras = frase.split() 
    palavras_embaralhadas = []
    
    for palavra in palavras:
        if len(palavra) > 2:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            meio = list(palavra[1:-1]) 
            random.shuffle(meio) 
            palavra_embaralhada = primeira_letra + ''.join(meio) + ultima_letra
        else:
            palavra_embaralhada = palavra
        
        palavras_embaralhadas.append(palavra_embaralhada)

    return ' '.join(palavras_embaralhadas)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
