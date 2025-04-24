
# Atribuindo um número float
numero = 10.0

# Verifica se o número é inteiro (mesmo sendo float)
# Exemplo: 10.0 é float, mas representa um número inteiro

if numero.is_integer():
    print("É um número inteiro (mesmo sendo float)!")
else:
    print("Não é inteiro.")

# CPF escrito como string (para simular entrada de usuário)
cpf_02 = "400038624er"

# Verifica se todos os caracteres da string são dígitos numéricos
if cpf_02.isdigit():
    print("É um número válido (só contém dígitos).")
else:
    print("Contém caracteres não numéricos.")