# A biblioteca `statistics` fornece funções prontas para realizar cálculos estatísticos básicos.
# Entre suas principais funções estão:
# - mean(): calcula a média aritmética dos valores.
# - median(): retorna o valor central de uma sequência ordenada.
# - mode(): retorna o valor que mais se repete na sequência.
# É uma ferramenta útil para análises iniciais de dados sem a necessidade de bibliotecas mais complexas como pandas ou numpy.

import statistics

lista = [20, 44, 34, 78, 55, 3, 88, 99, 99]

print(statistics.mean(lista))

print(statistics.mode(lista))

print(statistics.median(lista))

if 100 not in lista:
    lista.append(100)
else:
    ("Já contem o numero desejado!")
print(lista)