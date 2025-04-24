# Lista de números inteiros

lista = [20, 44, 34, 78, 55, 3, 88, 99, 99]

# Verifica se o número 100 já está presente na lista
if 100 not in lista:
    # Se não estiver, adiciona o número 100 à lista
    lista.append(100)
else:
    # Se já estiver, exibe uma mensagem informando
    print("Já contém o número desejado!")


print(lista)