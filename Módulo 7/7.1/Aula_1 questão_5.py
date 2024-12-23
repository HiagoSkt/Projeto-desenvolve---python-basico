
frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
indices_vogais = []

for i, char in enumerate(frase):
    if char in vogais:
        indices_vogais.append(i)

print(f"{len(indices_vogais)} vogais")
print(f"Índices {indices_vogais}")
