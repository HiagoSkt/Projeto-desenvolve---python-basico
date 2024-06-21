
distancia = float(input("Insira a distância da entrega em quilômetros: "))

peso = float(input("Insira o peso do pacote em quilogramas: "))

if distancia <= 100:
    valor_frete = peso * 1.00
elif 101 <= distancia <= 300:
    valor_frete = peso * 1.50
else:
    valor_frete = peso * 2.00

if peso > 10:
    valor_frete += 10.00

print(f"Valor do frete: R${valor_frete:.2f}")
