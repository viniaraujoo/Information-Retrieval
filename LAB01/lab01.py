import csv

noticias = open('noticias_estadao.csv')
leitura = csv.reader(noticias)
for linha in leitura:
    print linha 