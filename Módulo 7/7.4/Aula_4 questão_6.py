import csv

def musica_mais_tocada_por_ano(arquivo_csv):
    musica_mais_tocada = {}

    with open(arquivo_csv, mode='r', encoding='latin-1') as file:
        reader = csv.reader(file)
        next(reader)

        for linha in reader:
            if len(linha) != 10:
                continue

            track_name = linha[0]
            artist_name = linha[1]
            released_year = int(linha[3])
            streams = int(linha[8])

            if '"' in track_name or '"' in artist_name:
                continue

            if 2012 <= released_year <= 2022:
                if released_year not in musica_mais_tocada:
                    musica_mais_tocada[released_year] = [track_name, artist_name, released_year, streams]
                else:
                    if streams > musica_mais_tocada[released_year][3]:
                        musica_mais_tocada[released_year] = [track_name, artist_name, released_year, streams]

    lista_resultado = [musica_mais_tocada[ano] for ano in range(2012, 2023)]

    return lista_resultado

arquivo_csv = 'spotify-2023.csv'

resultado = musica_mais_tocada_por_ano(arquivo_csv)

for musica in resultado:
    print(musica)
