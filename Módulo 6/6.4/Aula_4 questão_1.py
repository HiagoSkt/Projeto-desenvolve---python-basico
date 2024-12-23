pares = [x for x in range(20, 51) if x % 2 == 0]
print("Números pares entre 20 e 50:", pares)

quadrados = [x**2 for x in range(1, 10)]
print("Quadrados dos valores de 1 a 9:", quadrados)

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)

par_ou_impar = ['par' if x % 2 == 0 else 'ímpar' for x in range(0, 30, 3)]
print("Par ou ímpar para números em range(0, 30, 3):", par_ou_impar)
