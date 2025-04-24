# A função lambda em Python permite criar funções anônimas de forma rápida e concisa.
# Ela aceita apenas uma expressão (sem comandos múltiplos ou blocos).
# É útil para funções simples, geralmente usadas temporariamente.

soma = lambda valor_1, valor_2: valor_1 + valor_2
print(soma(50, 50))


par_ou_ímpar = lambda valor: "Verdadeiro" if valor % 2 == 0 else "False" 
print(par_ou_ímpar(100))