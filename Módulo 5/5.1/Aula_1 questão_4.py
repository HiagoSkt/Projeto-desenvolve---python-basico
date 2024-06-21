from datetime import datetime

agora = datetime.now()

dia = agora.day
mes = agora.month
ano = agora.year
hora = agora.hour
minuto = agora.minute

data_formatada = f"Data: {dia:02}/{mes:02}/{ano}"

hora_formatada = f"Hora: {hora:02}:{minuto:02}"

print(data_formatada)
print(hora_formatada)
