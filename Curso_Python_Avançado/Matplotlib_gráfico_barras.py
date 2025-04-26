#Importando a biblioteca Matplotlib 
import matplotlib.pyplot as plt

#Gerando uma lista de compreensão com o laço for, verificando o tipo e imprimindo na tela 
valor = [valor for valor in range(30, 200, 17)]
print(type(valor))
print(valor)

#Configurando o largura e altura do gráfico 
plt.figure(figsize=(10, 5))

#Criando o grafico de linha a partir dos valores da lista, definindo cor, estilo da linha, marcador e a legenda
plt.plot(valor, color="green", linestyle="--", marker="o", label="Acompanhamento Mensal de Vendas")


#Adiciona valores acima de cada marcador no gráfico
for i, v in enumerate(valor):
    plt.text(i, v + 6, str(v), ha="center", fontsize=9, color="darkorange")

#Definindo o titulo, tamanho do mesmo e a fonte
plt.title("Vendas Mensais", fontsize=15, fontweight="bold")

#Rótulo do eixo Y e tamanho da fonte
plt.ylabel("Valores", fontsize=12)

#Rótulo do eixo X e tamanho da fonte
plt.xlabel("Dias", fontsize=12)

#Criando uma grade para o gráfico
plt.grid(True)

#Definindo o local da legenda e criando um titulo a ela 
plt.legend(loc="upper left", title="Vendas")

#Chamando a visualização do gráfico
plt.show()