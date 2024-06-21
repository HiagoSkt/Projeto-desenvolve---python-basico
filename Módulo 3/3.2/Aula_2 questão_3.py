
idade = int(input())

jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")

if jogou_tres_jogos == "True":
    jogou_tres_jogos = True
else:
    jogou_tres_jogos = False

vitorias = int(input("Quantos jogos já venceu? "))

if 16 <= idade <= 18 and jogou_tres_jogos and vitorias >= 1:
    apto = True
else:
    apto = False

print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")
