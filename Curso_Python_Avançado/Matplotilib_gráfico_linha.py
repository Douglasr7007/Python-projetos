import matplotlib.pyplot as plt

valores = [10, 15, 7, 25]

plt.plot(valores, color="red", linestyle="--", marker="o")        #Cria o gráfico de linha / Define a linha como vermelha, tracejada e com o marcado O
plt.title("Exemplo")                                              #Cria o titulo 
plt.xlabel("Dias")                                                #Eixo X
plt.ylabel("Vendas")                                              #Eixo Y
plt.grid(True)                                                    #Grade de fundo
plt.show()                                                        #Visualiza o gráfico
