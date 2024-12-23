import random

def carregar_palavras():
    with open('gabarito_forca.txt', 'r') as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip() for palavra in palavras]

def carregar_enforcado():
    with open('gabarito_enforcado.txt', 'r') as arquivo:
        return arquivo.read().split('\n\n')

def imprime_enforcado(erros):
    estagios = carregar_enforcado()
    print(estagios[erros])

def jogar_forca():
    palavras = carregar_palavras()
    palavra_secreta = random.choice(palavras)
    palavra_progresso = ['_'] * len(palavra_secreta)
    tentativas = 6 
    letras_erradas = []

    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem", len(palavra_secreta), "letras.")
    
    while tentativas > 0:
        print("\nPalavra: " + " ".join(palavra_progresso))
        print("Letras erradas: ", " ".join(letras_erradas))
        imprime_enforcado(6 - tentativas)
        
        tentativa = input("Digite uma letra: ").lower()
   
        if tentativa in letras_erradas or tentativa in palavra_progresso:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if tentativa in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == tentativa:
                    palavra_progresso[i] = tentativa
            print(f"Boa! A letra {tentativa} está na palavra.")
        else:
            letras_erradas.append(tentativa)
            tentativas -= 1
            print(f"A letra {tentativa} não está na palavra.")
        
        if '_' not in palavra_progresso:
            print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
            break

    if tentativas == 0:
        imprime_enforcado(6)
        print("\nVocê foi enforcado! A palavra era:", palavra_secreta)

jogar_forca()
