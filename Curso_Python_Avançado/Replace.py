# Comenta o código que imprime a frase "Hola Mundo!" seguida de uma saudação
#print("Hola Mundo!\nTudo bem?" )

# Define uma lista com os números de 1 a 9

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cria um dicionário com informações sobre uma pessoa

dicionário = {"nome" : "Douglas",
              "idade" : 25,
              "CPF" : 70074633120}

# Define uma string com uma frase motivacional

prioridades = "Vou me tornar um analista foda!"

# Comenta o código que imprime a variável 'prioridades' e extrai uma parte da string
print(prioridades)
print(prioridades[10:15])

# Cria a variável 'ola' com a frase "Hola Mundo!"

ola = "Hola Mundo!"


# Formatação/extração: remove a parte "cpf: " da string e converte o restante para um número inteiro

cpf = "cpf: 70074633120"
cpf_novo = int(cpf.replace("cpf: ", ""))

# Imprime o número de CPF sem o prefixo "cpf: "

print(cpf_novo)


