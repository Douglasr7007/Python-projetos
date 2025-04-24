 # O loop percorre os números de 5 a 95 (não chega a 100),
    # de 5 em 5. A cada iteração, imprime o número atual.

for n in range(5, 100, 5):
    print(f"Número:{n}")


# O enumerate percorre a lista 'pais', retornando o índice 'i' e o nome 'n' de cada país.
# O índice começa de 1 devido ao parâmetro '1' no enumerate.
# Em seguida, imprime o índice e as três primeiras letras do nome do país em maiúsculas.

pais = ["brasil", "mexico", "colombia", "paraguai", "peru", "argentina"]

for i, n in enumerate(pais, 1):
    print(f"{i}° {n.upper()[0:3]}")

    # Se o nome do país for "brasil", imprime uma mensagem especial sobre o Brasil ser hexacampeão.
    
    if n == "brasil":
        print(f"{n.upper()} é hexa campeão da copa do mundo!")



# Utiliza uma compreensão de lista para gerar uma lista de números pares de 0 até 98.
# O range(0, 100, 2) cria uma sequência de números de 0 a 100, com incremento de 2.

lista = [numero for numero in range(0, 100, 2)]
print(lista)

# O loop percorre os índices da lista 'pais', começando do 0 até o tamanho da lista,
# mas com incremento de 2. Ou seja, ele acessa apenas os índices pares da lista.

for n in range(0, (len(pais)),2):
    print(pais[n])