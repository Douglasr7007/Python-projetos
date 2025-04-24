# Função sem parâmetros (chamada direta, sempre exibe a mesma mensagem)

def boas_vindas():
    print("******** Python ******")

boas_vindas()

# Função com entrada de dados via input (sem parâmetros)

def soma():
    valor1 = int(input("Digite um número:"))
    valor2 = int(input("Digite outro número:"))
    resultado = valor1 + valor2
    print("O resultado é:", resultado)

soma()

# Outra função sem parâmetros, que realiza multiplicação com valores inseridos pelo usuário

def multiplicação():
    mult_1 = int(input("Digite um valor:"))
    mult_2 = int(input("Digite outro valor:"))
    resultado = mult_1 * mult_2
    print("O valor é:", resultado)
multiplicação()

# Função com parâmetros (dados são passados diretamente na chamada)

def somaa(valor01, valor02):
    resultado = valor01 + valor02
    print(resultado)
somaa(60, 60)


# Gerando 10 valores aleatórios e somando pares de números aleatórios

for loop in range(0, 10):

    import random

    x = random.random() #Gera números aleatórios entre 0 e 1 
    y = random.random()
    resultado = x + y
    print(resultado)
