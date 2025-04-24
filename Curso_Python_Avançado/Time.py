# Importa o módulo time, que fornece funções relacionadas ao tempo

import time

# Define duas variáveis de tempo

tempo1 = 5 
tempo2 = 10

# Verifica se tempo1 é maior que tempo2 e imprime a mensagem apropriada

if tempo1 > tempo2:
    print(f"O número {tempo1} é maior que o número {tempo2}")
else:

    # Se tempo2 for maior, imprime essa informação
    print(f"O número {tempo2} é maior que o número {tempo1}")

# Aguarda 3 segundos antes de imprimir a próxima mensagem

time.sleep(3)


# Imprime uma mensagem final dizendo que tempo2 é o maior

print(f"O número {tempo2} é o maior!")