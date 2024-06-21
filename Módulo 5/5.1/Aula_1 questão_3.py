import random

numero_aleatorio = random.randint(1, 10)
tentativas = 0
    
while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1
        
    if palpite < numero_aleatorio:
        print("Muito baixo, tente novamente!")
    elif palpite > numero_aleatorio:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {numero_aleatorio}.")
        break
    
print(f"Você acertou em {tentativas} tentativa(s).")
