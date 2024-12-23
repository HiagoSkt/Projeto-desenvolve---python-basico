def calcular_primeiro_digito(cpf):
    multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(9))
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

def calcular_segundo_digito(cpf, primeiro_digito):
    multiplicadores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(9)) + (primeiro_digito * multiplicadores[9]) 
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"

    primeiro_digito = calcular_primeiro_digito(cpf)
    segundo_digito = calcular_segundo_digito(cpf, primeiro_digito)
    
    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        return "Válido"
    else:
        return "Inválido"

cpf_usuario = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")

resultado = validar_cpf(cpf_usuario)
print(f"CPF {resultado}")
