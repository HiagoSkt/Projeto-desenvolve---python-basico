import string

def verificar_palindromo(frase):
    frase = frase.lower()
    frase = ''.join([c for c in frase if c.isalnum()])
    
    return frase == frase[::-1]

while True:
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")
    
    if frase.lower() == 'fim':
        break

    if verificar_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')

