import csv

livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 512],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1137],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 552],
    ["O Grande Gatsby", "F. Scott Fitzgerald", 1925, 180],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["Ensaio Sobre a Cegueira", "José Saramago", 1995, 318]
]

nome_arquivo = "meus_livros.csv"

with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    
    escritor.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    escritor.writerows(livros)

print(f"Arquivo '{nome_arquivo}' foi criado com sucesso!")
