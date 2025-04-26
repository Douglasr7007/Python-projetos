import numpy as np
import pandas as pd 

#Verica a versão do numpy 
print(np.__version__)


# Cria um array com 1 dimensão e 5 elementos 
array = np.array([10, 20, 30, 40, 50])
print(array)

# Cria um array com 2 dimensão e 5 elementos cada uma  
dimendões_2 = np.array([[50,60,70,80,90],[20,30,40,50,60]])
print(dimendões_2)


#Cria um array com 3 dimensões e 6 elementos cada uma  
dimensões_3 = np.array([
    [22,44,77,66,11,99],
    [33,22,11,77,60,80],
    [22,55,77,99,60,43,]
    ])

print(dimensões_3)


#Gerando 1 milhão de observações com o numpy arange e verificando o tamanho do mesmo com a função len 
um_milhao = np.arange(100000)
print(len(um_milhao))


#Acessar os arrays 
print(dimensões_3[0][3:])


#Verificando as dimensões e registros 
print(dimendões_2.shape)

#Operações vetorizadas com arrays 
multiplicação = dimendões_2 * 2 
print(multiplicação)

multiplicação_teste = dimendões_2[0][1:2] / 2
print(multiplicação_teste)

#Só é possivel fazer operações vetorizadas com arrays com a mesma quantidade de dimensões e elementos 
multiplicação = dimendões_2 * dimendões_2
print(multiplicação)


#O loop for item in dimendões_2.flat percorre todos os elementos do array de forma linear,
#sem se importar com a estrutura de linhas e colunas do array original.
for v in dimendões_2.flat:
    print(v)


df = pd.DataFrame(dimendões_2, columns=["A", "B", "C", "D", "E"])
print(df.loc[1, "E"])
print(df)