
Genêro = input()
Idade = int(input())
Tempo = int(input())

a = (Genêro == 'm' and Idade >= 65) or (Genêro == 'f' and Idade >= 60)
b = Tempo > 30
c = Idade >= 65 and Tempo >= 25

pode_aposentar = a or b or c

print(pode_aposentar)
    