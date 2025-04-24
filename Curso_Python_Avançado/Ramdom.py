# Importa o módulo random, que fornece funções para gerar números aleatórios

import random

# Escolhe um elemento aleatório da lista

lista = [2,3,4,5,6,7,8,43,2,5,6,66,55,8,8,88,3,3,22]
print(random.choice(lista))

# Gera um número inteiro aleatório entre 1 e 50 (inclusive)

print(random.randint(1,50))

# Escolhe 5 elementos aleatórios da lista (sem repetição)

print(random.sample(lista, 5))

# Gera um número de ponto flutuante aleatório entre 0 e 1

print(random.random())

