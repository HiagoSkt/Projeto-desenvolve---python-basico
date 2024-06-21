import random
from math import sqrt

def calcular_raiz_quadrada_soma(n):
    
    valores = [random.randint(0, 100) for _ in range(n)]
  
    soma = sum(valores)
    
    raiz_quadrada_soma = sqrt(soma)

    return raiz_quadrada_soma

n = int(input("Digite o valor de n (quantidade de valores aleatórios): "))

resultado = calcular_raiz_quadrada_soma(n)
print(f"A raiz quadrada da soma dos {n} valores aleatórios é: {resultado:.2f}")
