
Valor = int(input("Digite o valor"))

Notas_100 = Valor // 100
Valor = Valor % 100

Notas_50 = Valor // 50
Valor = Valor % 50

Notas_20 = Valor // 20
Valor = Valor % 20

Notas_10 = Valor // 10
Valor = Valor % 10

Notas_5 = Valor // 5
Valor = Valor % 5

Notas_2 = Valor // 2
Valor = Valor % 2

Notas_1 = Valor // 1
Valor = Valor % 1

print(f"{Notas_100} notas de 100")
print(f"{Notas_50} notas de 50")
print(f"{Notas_20} notas de 20")
print(f"{Notas_10} notas de 10")
print(f"{Notas_5} notas de 5")
print(f"{Notas_2} notas de 2")
print(f"{Notas_1} notas de 1")