
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")

forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if classe == "guerreiro":
    atributos = forca >= 15 and magia <= 10
elif classe == "mago":
    atributos = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    atributos = 5 < forca <= 15 and 5 < magia <= 15
else:
    atributos = False

print(f"Pontos de atributos com a classe escolhida: {atributos}")
