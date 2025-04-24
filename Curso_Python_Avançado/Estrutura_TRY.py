# O TRY permite testar um bloco de códigos quanto a erros

# O EXCEPT permite que vc lide com o erro 

# O FINALLY permite que vc excute o bloco de código, independete dos resultados dos blocos de TRY e EXCEPT 

# O ELSE é execultado quando não é atendida nenhuma condições dos blocos anteriores 


try: 
    print(4/0)

except:
    print("Não deu certo meu código!!!")

finally:
    print("Vou ser executado da independete de erros ou não!!!!") 
