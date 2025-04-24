# O laço while executa repetidamente enquanto uma determinada condição for verdadeira.
# Pode ser usado para criar loops finitos ou infinitos, dependendo da lógica aplicada.
# É possível incluir condições adicionais, listas, expressões e outros elementos dentro do bloco do loop.

contador = 0 

while contador <= 10:
    print(contador)
    contador+=1 

    if contador == 5:
        for c in range(10):
            print(c)
            