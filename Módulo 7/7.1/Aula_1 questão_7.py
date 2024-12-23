import random

def encrypt(nomes):

    chave_aleatoria = random.randint(1, 10)

    def criptografar(nome, chave):
        nome_criptografado = ""
        for char in nome:
            novo_char = ord(char) + chave
            if novo_char > 126:
                novo_char = 33 + (novo_char - 127)
            nome_criptografado += chr(novo_char)
        return nome_criptografado

    nomes_criptografados = [criptografar(nome, chave_aleatoria) for nome in nomes]
    
    return nomes_criptografados, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)

print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")
