import numpy as np
import time

# Criando uma lista com 1 milhão de números
lista = list(range(1000000))

# Criando um array com 1 milhão de números
array = np.arange(1000000)

# Tempo para multiplicar a lista por 2 (usando list comprehension)
inicio_lista = time.time()
nova_lista = [x * 2 for x in lista]
fim_lista = time.time()

# Tempo para multiplicar o array por 2
inicio_array = time.time()
novo_array = array * 2
fim_array = time.time()

print("Tempo com lista:", fim_lista - inicio_lista)
print("Tempo com array:", fim_array - inicio_array)