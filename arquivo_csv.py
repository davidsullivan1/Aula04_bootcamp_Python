import csv


pathFile = "exemplocsv.csv"


arquivo_csv: list = []

with open(file=pathFile, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)